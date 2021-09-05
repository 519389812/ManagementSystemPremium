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
    search_fields = ('user__full_name', 'reward__name', 'reward__type', 'title', 'content')
    # autocomplete_fields = ['user']
    readonly_fields = ('id', 'created_datetime', 'created_user')
    # list_filter = (
    #     ('date', DateRangeFilter), 'user__team', 'reward__type', 'reward'
    # )


class RewardSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/reward_penalty_summary_change_list.html"

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
            qs.values('user__full_name').annotate(**metrics).order_by('-score')
        )
        return response


class PenaltyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'penalty', 'score', 'title', 'content', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'penalty', 'score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'penalty__name', 'penalty__type', 'title', 'content')
    # autocomplete_fields = ['user']
    readonly_fields = ('id', 'created_datetime', 'created_user')
    # list_filter = (
    #     ('date', DateRangeFilter), 'user__team', 'penalty__type', 'penalty'
    # )


class PenaltySummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/reward_penalty_summary_change_list.html"

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
            qs.values('user__full_name').annotate(**metrics).order_by('-score')
        )
        return response


class WorkloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'level', 'start_datetime', 'end_datetime', 'assigned_team', 'working_time', 'get_initial_workload', 'score', 'workload', 'bonus', 'man_hours', 'remark', 'created_datetime', 'verified')
    list_editable = ('verified',)
    # autocomplete_fields = ['user', 'position', 'assigned_team']
    search_fields = ('user__last_name', 'user__first_name')
    fields = ('id', 'user', 'position', 'get_position_rule', 'level', 'get_level_rule', 'start_datetime', 'end_datetime', 'assigned_team', 'remark', 'working_time', 'get_initial_workload', 'score', 'workload', 'bonus', 'man_hours', 'verified', 'created_datetime', 'verified_user', 'verified_datetime')
    readonly_fields = ('id', 'user', 'created_datetime', 'working_time', 'get_position_rule', 'get_initial_workload', 'get_level_rule', 'score', 'workload', 'bonus', 'man_hours', 'verified_user', 'verified_datetime')
    # list_filter = (
    #     ('start_datetime', DateTimeRangeFilter), 'assigned_team', 'position__type', 'position', 'verified'
    # )

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'working_time': '注意：工作时长超过24小时判定为无效!',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadRecordAdmin, self).get_form(request, obj, **kwargs)

    def get_initial_workload(self, obj):
        return '分数: %s, 工作量: %s, 奖金: %s, 计算工时: %s' % (
            obj.position.score, obj.position.workload, obj.position.bonus, "是" if obj.position.man_hours else "否")
    get_initial_workload.short_description = "基础分值"

    def get_position_rule(self, obj):
        return obj.position.rule if obj.position.rule else "无"
    get_position_rule.short_description = "岗位规则"

    def get_level_rule(self, obj):
        return obj.level.rule if obj.level else "无"
    get_level_rule.short_description = "程度规则"

    def get_weight_column(self, obj, model_name, column_name, working_time):
        is_count_time = False
        return_column = eval('obj.%s.%s' % (model_name, column_name))
        if eval('obj.%s.rule' % model_name):
            if eval('obj.%s.rule.date_condition' % model_name) or eval('obj.%s.rule.condition' % model_name):
                if eval('obj.%s.rule.date_condition' % model_name):
                    end_date = timezone.localtime(obj.start_datetime)
                    date_delta = int(re.findall(r'\d+', eval('obj.%s.rule.date_condition' % model_name))[0])
                    start_date = end_date - timezone.timedelta(date_delta)
                    count = WorkloadRecord.objects.filter(user=obj.user, start_datetime__gte=start_date, end_datetime__lte=end_date).count()
                else:
                    count = WorkloadRecord.objects.filter(user=obj.user).count()
                if eval('obj.%s.rule.condition' % model_name):
                    match = eval('count obj.%s.rule.condition' % model_name)
                    if match:
                        string = 'obj.%s.rule.%s' % (model_name, column_name)
                        return_column = eval('%s * %s %s' % (return_column, working_time, eval(string))) if eval(string) else return_column
                        is_count_time = True
                else:
                    if count > 0:
                        string = 'obj.%s.rule.%s' % (model_name, column_name)
                        return_column = eval('%s * %s %s' % (return_column, working_time, eval(string))) if eval(string) else return_column
                        is_count_time = True
            else:
                if eval('obj.%s.rule.%s' % (model_name, column_name)):
                    string = 'obj.%s.rule.%s' % (model_name, column_name)
                    return_column = eval('%s * %s %s' % (return_column, working_time, eval(string))) if eval(string) else return_column
                    is_count_time = True
        if not is_count_time:
            return_column = eval('%s * %s' % (return_column, working_time))
        if obj.level:
            if eval('obj.level.rule.%s' % column_name):
                string = 'obj.level.rule.%s' % column_name
                return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        return return_column

    def get_weight_man_hours(self, obj, working_time):
        if obj.position.rule:
            if obj.position.rule.man_hours:
                working_time = eval('%s %s' % (working_time, obj.position.rule.man_hours))
        if obj.level:
            if obj.level.rule.man_hours:
                working_time = eval('%s %s' % (working_time, obj.level.rule.man_hours))
        return working_time

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if obj.working_time > 24:
                messages.error(request, "保存失败！工作时长超过最大限制24小时！")
                messages.set_level(request, messages.ERROR)
                return
            if not change:
                super().save_model(request, obj, form, change)
            obj.score = round(self.get_weight_column(obj, 'position', 'score', obj.working_time), 2)
            obj.workload = round(self.get_weight_column(obj, 'position', 'workload', obj.working_time), 2)
            obj.bonus = round(self.get_weight_column(obj, 'position', 'bonus', obj.working_time), 2)
            if obj.position.man_hours:
                obj.man_hours = round(self.get_weight_man_hours(obj, obj.working_time), 2)
            else:
                obj.man_hours = 0
            verified_before = WorkloadRecord.objects.get(id=obj.id).verified
            verified_after = form.cleaned_data["verified"]
            if verified_before != verified_after and verified_after is True:
                obj.verified_user = request.user
                obj.verified_datetime = timezone.localtime(timezone.now())
            super().save_model(request, obj, form, change)


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
            'total_score': Sum('score'),
            'total_workload': Sum('workload'),
            'total_bonus': Sum('bonus'),
            'total_man_hours': Sum('man_hours'),
        }
        response.context_data['summary'] = list(
            qs.filter(verified=True).values("user__last_name", "user__first_name").annotate(**metrics).order_by('-total_workload')
        )
        return response


class OutputRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'output', 'get_output_rule', 'level', 'get_level_rule', 'quantity', 'weight_quantity', 'assigned_team', 'remark', 'verified')
    fields = ('id', 'user', 'date', 'output', 'get_output_rule', 'level', 'get_level_rule', 'quantity', 'weight_quantity', 'assigned_team', 'remark', 'created_datetime', 'verified', 'verified_user', 'verified_datetime')
    list_editable = ('verified',)
    list_display_links = ('user',)
    search_fields = ('user__last_name', 'user__first_name')
    readonly_fields = ('id', 'user', 'get_output_rule', 'get_level_rule', 'weight_quantity', 'created_datetime', 'verified_user', 'verified_datetime')
    # list_filter = (
    #     ('date', DateRangeFilter), 'assigned_team', 'output__type', 'output', 'verified'
    # )

    def get_output_rule(self, obj):
        return obj.output.rule if obj.output.rule else "无"
    get_output_rule.short_description = "产出规则"

    # 必须加入到readonly_fields内，否则会报错
    def get_level_rule(self, obj):
        return obj.level.rule if obj.level else "无"
    get_level_rule.short_description = "程度规则"

    def get_weight_column(self, obj, column_name):
        return_column = eval('obj.%s' % column_name)
        if obj.output.rule:
            if obj.output.rule.date_condition:
                end_date = obj.date
                date_delta = int(re.findall(r'\d+', obj.output.rule.date_condition)[0])
                start_date = end_date - timezone.timedelta(date_delta)
                count = OutputRecord.objects.filter(user=obj.user, date__gte=start_date, date__lte=end_date).count()
            else:
                count = OutputRecord.objects.filter(user=obj.user).count()
            if obj.output.rule.condition:
                match = eval('count %s' % obj.output.rule.condition)
                if match:
                    string = 'obj.output.rule.%s' % column_name
                    return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
            else:
                if count > 0:
                    string = 'obj.output.rule.%s' % column_name
                    return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        if obj.level:
            string = 'obj.level.rule.%s' % column_name
            return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        return return_column

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.weight_quantity = round(self.get_weight_column(obj, 'quantity'), 2)
            obj.user = request.user
            super().save_model(request, obj, form, change)


class OutputSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/output_summary_change_list.html"

    # list_filter = (
    #     ('date', DateTimeRangeFilter), 'user__team', 'output__type', 'output'
    # )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'weight_quantity': Sum('weight_quantity'),
        }
        response.context_data['summary'] = list(
            qs.filter(verified=True).values("user__last_name", "user__first_name").annotate(**metrics).order_by('-weight_quantity')
        )
        return response


admin.site.register(Shift, ShiftAdmin)
admin.site.register(OutputType, OutputTypeAdmin)
admin.site.register(Output, OutputAdmin)
admin.site.register(RewardRecord, RewardRecordAdmin)
admin.site.register(RewardSummary, RewardSummaryAdmin)
admin.site.register(WorkloadRecord, WorkloadRecordAdmin)
admin.site.register(WorkloadSummary, WorkloadSummaryAdmin)
admin.site.register(OutputRecord, OutputRecordAdmin)
admin.site.register(OutputSummary, OutputSummaryAdmin)
