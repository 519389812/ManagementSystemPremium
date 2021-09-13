from django.contrib import admin
from cost.models import CostType, Cost, CostRecord, CostSummary
from django.db.models import Count, Sum
from performance.admin import get_weight_column_value
from performance.models import RewardSummary, PenaltySummary, WorkloadRecord
import numpy as np
import pandas as pd


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    search_fields = ('name',)
    autocomplete_fields = ['type']


class CostRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    fields = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('team__name', 'cost__type__name', 'cost__name', 'create_user__full_name')
    autocomplete_fields = ['team', 'cost']
    readonly_fields = ('id', 'create_datetime', 'create_user')
    list_filter = ('date', 'team__name', 'cost__name')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.create_user = request.user
            super().save_model(request, obj, form, change)


class CostSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/cost_summary_change_list.html"

    list_filter = ('date', )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        filters_params = response.context_data['cl'].get_filters_params()
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        filter_string = ''
        if len(filters_params) > 0:
            for k, v in filters_params.items():
                filter_string += "%s='%s'," % (k, v)

        if len(qs) > 0:
            qs = pd.DataFrame(qs.values('team__id', 'team__name', 'cost__name', 'quantity')).rename(columns={'team__id': 'user__team__id', 'team__name': 'user__team__name'})
            qs = qs.pivot_table(values=['quantity'], columns=['cost__name'], index=['user__team__id', 'user__team__name'], aggfunc=np.sum).rename(columns={'score': 'workload_score'})
            columns_values = [v2 + '_' + v1 for v1, v2 in qs.columns.values]
            qs.columns = columns_values
        else:
            qs = None

        # workload
        workload_qs = eval('WorkloadRecord.objects.filter(%s)' % filter_string)

        reward_qs = eval('RewardSummary.objects.filter(%s)' % filter_string)
        value_list = get_weight_column_value(reward_qs, 'weight_score')
        for i in range(len(reward_qs)):
            RewardSummary.objects.filter(id=reward_qs[i].id).update(score=value_list[i])

        penalty_qs = eval('PenaltySummary.objects.filter(%s)' % filter_string)
        value_list = get_weight_column_value(penalty_qs, 'weight_score')
        for i in range(len(penalty_qs)):
            PenaltySummary.objects.filter(id=penalty_qs[i].id).update(score=value_list[i])

        # workload
        if len(workload_qs) > 0:
            workload_qs = pd.DataFrame(workload_qs.values('user__team__id', 'user__team__name',  'sale'))
            workload_qs = workload_qs.pivot_table(values=['sale'], index=['user__team__id', 'user__team__name'], aggfunc=np.sum)
        else:
            workload_qs = None

        # reward
        if len(reward_qs) > 0:
            reward_qs = pd.DataFrame(reward_qs.values('user__team__id', 'user__team__name', 'reward__type__name', 'score'))
            reward_qs = reward_qs.pivot_table(values=['user__team__id', 'score'], columns=['reward__type__name'], index=['user__team__id', 'user__team__name'], aggfunc={'user__team__id': 'count', 'score': np.sum}).rename(columns={'user__team__id': 'reward_count', 'score': 'reward_score'})
            columns_values = [v2 + '_' + v1 for v1, v2 in reward_qs.columns.values]
            reward_qs.columns = columns_values
        else:
            reward_qs = None

        # penalty
        if len(penalty_qs) > 0:
            penalty_qs = pd.DataFrame(penalty_qs.values('user__team__id', 'user__team__name', 'penalty__type__name', 'score'))
            penalty_qs = penalty_qs.pivot_table(values=['user__team__id', 'score'], columns=['penalty__type__name'], index=['user__team__id', 'user__team__name'], aggfunc={'user__team__id': 'count', 'score': np.sum}).rename(columns={'user__team__id': 'penalty_count', 'score': 'penalty_score'})
            columns_values = [v2 + '_' + v1 for v1, v2 in penalty_qs.columns.values]
            penalty_qs.columns = columns_values
        else:
            penalty_qs = None

        qs_list = [qs, workload_qs, reward_qs, penalty_qs]
        qs_list = [q for q in qs_list if q is not None]
        if len(qs_list) == 0:
            return response
        qs = qs_list[0]
        if len(qs_list) > 1:
            for i in range(1, len(qs_list)):
                qs = pd.merge(qs, qs_list[i], on=['user__team__id', 'user__team__name'], how='outer')

        qs.fillna('', inplace=True)

        qs_index_name = qs.index.names
        qs_index = qs.index.to_list()
        qs_value = qs.to_dict('records')
        for i in range(len(qs_index)):
            for j in range(len(qs_index_name)):
                qs_value[i][qs_index_name[j]] = qs_index[i][j]

        index_basic = ['user__team__id', 'user__team__name', 'sale']
        translate_dict = {'_quantity': '成本', '_reward_score': '奖励分', '_reward_count': '奖励量', '_penalty_score': '处罚分', '_penalty_count': '处罚量'}
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
                    del (qs_value[i][v])

        for k, v in translate_dict.items():
            for i in range(len(additional_column_list)):
                if k in additional_column_list[i]:
                    additional_column_list[i] = additional_column_list[i].replace(k, v)

        for i in range(len(qs_value)):
            qs_value[i]['additional'] = additional_data_list[i]

        response.context_data['summary'] = qs_value
        response.context_data['additional_column_list'] = additional_column_list
        return response


admin.site.register(CostType, CostTypeAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(CostRecord, CostRecordAdmin)
admin.site.register(CostSummary, CostSummaryAdmin)
