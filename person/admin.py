from django.contrib import admin
from performance.admin import get_weight_column_value
from django.contrib import messages
from django.shortcuts import render, redirect
from ManagementSystemPremium.views import parse_url_param


class PersonSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/person_summary_change_list.html"

    list_filter = (
        'date', 'create_datetime', 'position__name', 'position__type__name', 'verifier'
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        value_list = get_weight_column_value(qs, 'weight_score')
        for i in range(len(qs)):
            RewardRecord.objects.filter(id=qs[i].id).update(score=value_list[i])
        metrics = {
            'count': Count('user'),
            'score': Sum('score'),
        }
        data = list(qs.values('user__team__name', 'user__full_name').annotate(**metrics).order_by('-score'))
        response.context_data['summary'] = data
        return response
