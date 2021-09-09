from django.contrib import admin
from performance.admin import get_weight_column_value
from django.contrib import messages
from django.shortcuts import render, redirect
from ManagementSystemPremium.views import parse_url_param
from django.db.models import Count, Sum
from person.models import PersonSummary
from performance.models import RewardSummary, PenaltySummary
import pandas as pd
import numpy as np


class PersonSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/person_summary_change_list.html"

    list_filter = (
        'date', 'create_datetime', 'position__name', 'position__type__name', 'verifier'
    )

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

        if len(qs) > 0:
            qs = pd.DataFrame(qs.values('user__team__name', 'user__id', 'user__full_name', 'number_people', 'number_baggage', 'sale', 'score'))
            qs = qs.pivot_table(values=['number_people', 'number_baggage', 'sale', 'score'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc=np.sum).rename(columns={'score': 'workload_score'})
        else:
            qs = pd.DataFrame(None)
        if len(reward_qs) > 0:
            reward_qs = pd.DataFrame(reward_qs.values('user__team__name', 'user__id', 'user__full_name', 'score'))
            reward_qs = reward_qs.pivot_table(values=['user__id', 'score'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc={'user__id': 'count', 'score': np.sum}).rename(columns={'user__id': 'reward_count', 'score': 'reward_score'})
        else:
            reward_qs = pd.DataFrame(None)
        if len(penalty_qs) > 0:
            penalty_qs = pd.DataFrame(penalty_qs.values('user__team__name', 'user__id', 'user__full_name', 'score'))
            penalty_qs = penalty_qs.pivot_table(values=['user__id', 'score'], index=['user__team__name', 'user__id', 'user__full_name'], aggfunc={'user__id': 'count', 'score': np.sum}).rename(columns={'user__id': 'penalty_count', 'score': 'penalty_score'})
        else:
            penalty_qs = pd.DataFrame(None)
        if qs.shape[0] > 0:
            if reward_qs.shape[0] > 0:
                qs = pd.merge(qs, reward_qs, on=['user__team__name', 'user__id', 'user__full_name'], how='outer')
            if penalty_qs.shape[0] > 0:
                qs = pd.merge(qs, penalty_qs, on=['user__team__name', 'user__id', 'user__full_name'], how='outer')
        elif reward_qs.shape[0] > 0 and penalty_qs.shape[0] > 0:
            qs = pd.merge(reward_qs, penalty_qs, on=['user__team__name', 'user__id', 'user__full_name'], how='outer')
        elif reward_qs.shape[0] == 0 and penalty_qs.shape[0] == 0:
            return response
        else:
            if reward_qs.shape[0] > 0:
                qs = reward_qs
            else:
                qs = penalty_qs
        qs_index_name = qs.index.names
        qs_index = qs.index.to_list()
        qs_value = qs.to_dict('records')
        for i in range(len(qs_index)):
            for j in range(len(qs_index_name)):
                qs_value[i][qs_index_name[j]] = qs_index[i][j]
        response.context_data['summary'] = qs_value
        print(qs_value)
        return response


admin.site.register(PersonSummary, PersonSummaryAdmin)
