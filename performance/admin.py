from django.contrib import admin
from rule.models import PositionType, Position, RewardType, Reward, PenaltyType, Penalty
from performance.models import RewardRecord, RewardSummary, PenaltyRecord, PenaltySummary, WorkloadRecord, WorkloadSummary
from team.models import CustomTeam
from user.models import CustomUser
from django.contrib.admin import widgets
from django.db.models import Count, Sum, DateTimeField, DateField, Min, Max, Avg, F, ExpressionWrapper, fields, Value, Func
from django.db.models.functions import Trunc
from django.apps import apps
from django.utils import timezone
import re
from django.contrib import messages
import math


def half_ceil(x):
    return math.modf(x)[1] + (0.5 if math.modf(x)[0] < 0.5 else 1)


class RewardRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'reward', 'score', 'title', 'content', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'reward', 'score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'reward__name', 'reward__type__name', 'title', 'content')
    # autocomplete_fields = ['user']
    readonly_fields = ('id', 'create_datetime', 'create_user')
    # list_filter = (
    #     ('date', DateRangeFilter), 'user__team', 'reward__type', 'reward'
    # )


class RewardSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/reward_summary_change_list.html"

    # list_filter = (
    #     ('date', DateTimeRangeFilter), 'user__team', 'reward__type', 'reward'
    # )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'score': Sum('score'),
        }
        response.context_data['summary'] = list(
            qs.values('user__team__name').values('user__full_name').values('reward__name').annotate(**metrics).order_by('-score')
        )
        return response


class PenaltyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'penalty', 'score', 'title', 'content', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'penalty', 'score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'penalty__name', 'penalty__type__name', 'title', 'content')
    # autocomplete_fields = ['user']
    readonly_fields = ('id', 'create_datetime', 'create_user')
    # list_filter = (
    #     ('date', DateRangeFilter), 'user__team', 'penalty__type', 'penalty'
    # )


class PenaltySummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/penalty_summary_change_list.html"

    # list_filter = (
    #     ('date', DateTimeRangeFilter), 'user__team', 'reward__type', 'reward'
    # )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'score': Sum('score'),
        }
        response.context_data['summary'] = list(
            qs.values('user__team__name').values('user__full_name').values('penalty__name').annotate(**metrics).order_by('-score')
        )
        return response


class WorkloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    # autocomplete_fields = ['user', 'position', 'assigned_team']
    search_fields = ('user__full_name', 'position__name', 'position__type__name', 'verifier__name', 'remark', 'verify_user__name')
    fields = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    readonly_fields = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'create_datetime', 'verify_user', 'verify_datetime')
    # list_filter = (
    #     ('start_datetime', DateTimeRangeFilter), 'assigned_team', 'position__type', 'position', 'verified'
    # )

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'date': '请以开始工作日期为准!',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadRecordAdmin, self).get_form(request, obj, **kwargs)


class WorkloadSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/workload_summary_change_list.html"

    # list_filter = (
    #     ('start_datetime', DateTimeRangeFilter), 'user__team', 'position__type', 'position'
    # )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'number_people': Sum('number_people'),
            'number_baggage': Sum('number_baggage'),
            'sale': Sum('sale'),
        }
        response.context_data['summary'] = list(
            qs.filter(verified=True).values('user__team__name').values('user__full_name').annotate(**metrics).order_by('-sale')
        )
        return response


admin.site.register(RewardRecord, RewardRecordAdmin)
admin.site.register(RewardSummary, RewardSummaryAdmin)
admin.site.register(PenaltyRecord, PenaltyRecordAdmin)
admin.site.register(PenaltySummary, PenaltySummaryAdmin)
admin.site.register(WorkloadRecord, WorkloadRecordAdmin)
admin.site.register(WorkloadSummary, WorkloadSummaryAdmin)
