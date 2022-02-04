from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render, redirect
from ManagementSystemPremium.views import parse_url_param
from django.db.models import Count, Sum
from person.models import SkillType, Skill, Employee, EmployeeSummary
import pandas as pd
import numpy as np
import collections


class PersonSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/person_summary_change_list.html"

    list_filter = ('date',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        filters_params = response.context_data['cl'].get_filters_params()
        try:
            qs = response.context_data['cl'].queryset.filter(verify=True)
        except (AttributeError, KeyError):
            return response

        filter_string = ''
        if len(filters_params) > 0:
            for k, v in filters_params.items():
                filter_string += "%s='%s'," % (k, v)

        reward_qs = eval('RewardSummary.objects.filter(%s)' % filter_string)
        value_list = get_weight_column_value(reward_qs, 'weight_score')
        for i in range(len(reward_qs)):
            RewardSummary.objects.filter(id=reward_qs[i].id).update(score=value_list[i])

        penalty_qs = eval('PenaltySummary.objects.filter(%s)' % filter_string)
        value_list = get_weight_column_value(penalty_qs, 'weight_score')
        for i in range(len(penalty_qs)):
            PenaltySummary.objects.filter(id=penalty_qs[i].id).update(score=value_list[i])

        # workload
        if len(qs) > 0:
            qs = pd.DataFrame(qs.values('user__team__name', 'user__id', 'user__full_name', 'number_people', 'number_baggage', 'sale', 'score'))
            qs = qs.pivot_table(values=['number_people', 'number_baggage', 'sale', 'score'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc=np.sum).rename(columns={'score': 'workload_score'})
        else:
            qs = None

        # reward
        if len(reward_qs) > 0:
            reward_qs = pd.DataFrame(reward_qs.values('user__team__name', 'user__id', 'user__full_name', 'reward__type__name', 'score'))
            reward_qs = reward_qs.pivot_table(values=['user__id', 'score'], columns=['reward__type__name'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc={'user__id': 'count', 'score': np.sum}).rename(columns={'user__id': 'reward_count', 'score': 'reward_score'})
            columns_values = [v2 + '_' + v1 for v1, v2 in reward_qs.columns.values]
            reward_qs.columns = columns_values
        else:
            reward_qs = None

        # penalty
        if len(penalty_qs) > 0:
            penalty_qs = pd.DataFrame(penalty_qs.values('user__team__name', 'user__id', 'user__full_name', 'penalty__type__name', 'score'))
            penalty_qs = penalty_qs.pivot_table(values=['user__id', 'score'], columns=['penalty__type__name'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc={'user__id': 'count', 'score': np.sum}).rename(columns={'user__id': 'penalty_count', 'score': 'penalty_score'})
            columns_values = [v2 + '_' + v1 for v1, v2 in penalty_qs.columns.values]
            penalty_qs.columns = columns_values
        else:
            penalty_qs = None

        # training
        training_qs = eval('Training.objects.filter(%s)' % filter_string)
        if len(training_qs) > 0:
            training_qs = pd.DataFrame(training_qs.values('name', 'date', 'user__team__name', 'user__id', 'user__full_name'))
            training_qs['date'] = training_qs['date'].apply(str)
            training_qs['training'] = training_qs['date'] + ' ' + training_qs['name']
            training_qs['training__name'] = training_qs['date'] + ' ' + training_qs['name']
            training_qs = training_qs[['training', 'training__name', 'user__team__name', 'user__id', 'user__full_name']]
            training_qs = training_qs.pivot_table(values=['training'], columns=['training__name'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc='count')
            columns_values = [v for _, v in training_qs.columns.values]
            training_qs.columns = columns_values
        else:
            training_qs = None

        qs_list = [qs, reward_qs, penalty_qs, training_qs]
        qs_list = [q for q in qs_list if q is not None]
        if len(qs_list) == 0:
            return response
        qs = qs_list[0]
        if len(qs_list) > 1:
            for i in range(1, len(qs_list)):
                qs = pd.merge(qs, qs_list[i], on=['user__team__name', 'user__id', 'user__full_name'], how='outer')

        qs.fillna('', inplace=True)
        qs_index_name = qs.index.names
        qs_index = qs.index.to_list()
        qs_value = qs.to_dict('records')
        for i in range(len(qs_index)):
            for j in range(len(qs_index_name)):
                qs_value[i][qs_index_name[j]] = qs_index[i][j]

        index_basic = ['number_baggage', 'number_people', 'sale', 'workload_score', 'user__team__name', 'user__id', 'user__full_name']
        translate_dict = {'_reward_score': '奖励分', '_reward_count': '奖励量', '_penalty_score': '处罚分', '_penalty_count': '处罚量'}
        additional_column_list = []
        additional_data_list = []

        collect_column = True
        for i in range(len(qs_value)):
            template_data_list = []
            for k, v in qs_value[i].items():
                if k not in index_basic:
                    if collect_column:
                        additional_column_list.append(k)
                    template_data_list.append(v)
            if len(additional_column_list) > 0:
                collect_column = False
            additional_data_list.append(template_data_list)

        for i in range(len(additional_data_list)):
            for v in additional_column_list:
                if v in qs_value[i].keys():
                    del(qs_value[i][v])

        for k, v in translate_dict.items():
            for i in range(len(additional_column_list)):
                if k in additional_column_list[i]:
                    additional_column_list[i] = additional_column_list[i].replace(k, v)

        for i in range(len(qs_value)):
            qs_value[i]['additional'] = additional_data_list[i]

        response.context_data['summary'] = qs_value
        response.context_data['additional_column_list'] = additional_column_list
        return response


class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    search_fields = ('name',)
    autocomplete_fields = ['type']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    fields = ('id', 'user')
    list_display_links = ('id',)
    filter_horizontal = ('skill',)
    search_fields = ('user__full_name',)
    autocomplete_fields = ['user']
    readonly_fields = ('id',)
    list_filter = ('user__team',)


class EmployeeSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/employee_summary_change_list.html"

    list_filter = ('user__team',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('user__full_name', 'skill'))
        qs = qs.pivot_table(values=['training'], columns=['skill__name'],
                            index=['user__team__name', 'user__id', 'user__full_name'], aggfunc='count')

        metrics = {
            'cost': Count('cost'),
            'quantity': Sum('quantity'),
        }
        data = list(
            qs.filter(user__is_active=True).values('team__name').annotate(**metrics).order_by('-quantity'))
        response.context_data['summary'] = data
        return response


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Employee, EmployeeAdmin)
