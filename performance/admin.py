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


def get_weight_column(obj, column_name, model_name, model_column):
    return_column = eval('obj.%s.%s' % (model_column, column_name))
    if eval('obj.%s.repeat_rule' % model_column):
        end_date = obj.date
        day_delta = eval('obj.%s.repeat_rule.day' % model_column)
        start_date = end_date - timezone.timedelta(day_delta)
        count = eval('%s.objects.filter(user=obj.user, %s=obj.%s, date__gte=start_date, date__lte=end_date, create_datetime__lt=obj.create_datetime).count()' % (model_name, model_column, model_column))
        if count > 0:
            string = 'obj.%s.repeat_rule.calculation' % model_column
            try:
                return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
            except:
                pass
    if obj.level_rule:
        string = 'obj.level_rule.calculation'
        try:
            return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        except:
            pass
    return return_column


def get_weight_column_value(qs, column_name):
    value_list = []
    for q in qs:
        value_list.append(eval('q.%s' % column_name))
    return value_list


class RewardRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'reward', 'level_rule', 'basic_score', 'weight_score', 'title', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'reward', 'level_rule', 'basic_score', 'weight_score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'reward__name', 'reward__type__name', 'title', 'content', 'level_rule__name')
    autocomplete_fields = ['user', 'reward', 'level_rule']
    readonly_fields = ('id', 'score', 'create_datetime', 'create_user', 'basic_score', 'weight_score')
    list_filter = (
        'date', 'user__team', 'reward__name', 'reward__type__name', 'level_rule__name'
    )

    # 必须要写入readonly_fields，否则报错
    def basic_score(self, obj):
        return obj.reward.score
    basic_score.short_description = '基础分数'

    def weight_score(self, obj):
        return get_weight_column(obj, 'score', 'RewardRecord', 'reward')
    weight_score.short_description = '加成后分数'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'level_rule': '同类奖励，程度不同加分不同时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RewardRecordAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.create_user = request.user
            super().save_model(request, obj, form, change)


class RewardSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/reward_summary_change_list.html"

    list_filter = (
        'date', 'user__team', 'reward__name', 'reward__type__name',
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


class PenaltyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'penalty', 'level_rule', 'basic_score', 'weight_score', 'title', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'penalty', 'level_rule', 'basic_score', 'weight_score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'penalty__name', 'penalty__type__name', 'title', 'content', 'level_rule__name')
    autocomplete_fields = ['user', 'penalty', 'level_rule']
    readonly_fields = ('id', 'score', 'create_datetime', 'create_user', 'basic_score', 'weight_score')
    list_filter = (
        'date', 'user__team', 'penalty__name', 'penalty__type__name', 'level_rule__name'
    )

    def basic_score(self, obj):
        return obj.penalty.score
    basic_score.short_description = '基础分数'

    def weight_score(self, obj):
        return get_weight_column(obj, 'score', 'PenaltyRecord', 'penalty')
    weight_score.short_description = '加成后分数'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'level_rule': '同类奖励，程度不同处罚不同时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(PenaltyRecordAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.create_user = request.user
            super().save_model(request, obj, form, change)


class PenaltySummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/penalty_summary_change_list.html"

    list_filter = (
        'date', 'user__team', 'penalty__name', 'penalty__type__name'
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        value_list = get_weight_column_value(qs, 'weight_score')
        for i in range(len(qs)):
            PenaltyRecord.objects.filter(id=qs[i].id).update(score=value_list[i])
        metrics = {
            'count': Count('user'),
            'score': Sum('score'),
        }
        data = list(
            qs.values('user__team__name', 'user__full_name').annotate(**metrics).order_by('-score'))
        print(data)
        response.context_data['summary'] = data
        return response


class WorkloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    autocomplete_fields = ['user', 'position', 'verifier', 'verify_user']
    search_fields = ('user__full_name', 'position__name', 'position__type__name', 'verifier__name', 'remark', 'verify_user__name')
    fields = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    readonly_fields = ('id', 'user', 'position', 'number_people', 'number_baggage', 'sale', 'create_datetime', 'verify_user', 'verify_datetime')
    list_filter = (
        'date', 'create_datetime', 'position__name', 'position__type__name', 'verifier'
    )

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'date': '请以开始工作日期为准!',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadRecordAdmin, self).get_form(request, obj, **kwargs)


class WorkloadSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/workload_summary_change_list.html"

    list_filter = (
        'date', 'create_datetime', 'position__name', 'position__type__name', 'verifier'
    )

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
