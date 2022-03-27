from django.contrib import admin
from performance.models import Position, WorkloadItem, WorkloadRecord, WorkloadSummary, ManHourItem, ManHourRecord, ManHourSummary
from team.models import CustomTeam
from user.models import CustomUser
from django.contrib.admin import widgets
from django.db.models.functions import Trunc
from django.apps import apps
from django.utils import timezone
import re
from django.contrib import messages
import math
import json
from django.db.models import Count, Sum, DateTimeField, DateField, Min, Max, Avg, F, ExpressionWrapper, fields, Value, Func
import pandas as pd
import numpy as np


def half_ceil(x):
    return math.modf(x)[1] + (0.5 if math.modf(x)[0] < 0.5 else 1)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class WorkloadItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name', 'weight')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'sale_rule': '当需要设置销量目标并转成分数时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadItemAdmin, self).get_form(request, obj, **kwargs)


class WorkloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'position', 'workload_project', 'output', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    autocomplete_fields = ['user', 'position', 'verifier', 'verify_user']
    search_fields = ('user__full_name', 'date', 'position__name', 'verifier__name', 'remark')
    fieldsets = (
        ('基本信息', {'fields': ['id', 'user', 'position', 'workload_project', 'verifier', 'verify', 'remark']}),
        ('操作信息', {'fields': ['create_datetime', 'verify_user', 'verify_datetime']}),
    )
    readonly_fields = ('id', 'user', 'position', 'workload_project', 'output', 'create_datetime', 'verify_user', 'verify_datetime')
    list_filter = (
        'date', 'create_datetime', 'position__name', 'verifier'
    )

    def workload_project(self, obj):
        return ' '.join(['%s: %s' % (k, v) for k, v in json.loads(obj.workload).items()])
    workload_project.short_description = '工作量'

    def output(self, obj):
        workload_item = list(WorkloadItem.objects.filter(position=obj.position).values('name', 'weight'))
        workload_item = {i['name']: i['weight'] for i in workload_item}
        out = sum([v * workload_item.get(k, 0) for k, v in json.loads(obj.workload).items()])
        return out
    output.short_description = '折算产出'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'date': '请以开始工作日期为准!',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadRecordAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if form.cleaned_data['verify']:
                obj.verify_user = request.user
                obj.verify_datetime = timezone.localtime(timezone.now())
            else:
                obj.verify_user = None
                obj.verify_datetime = None
            super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    # 未知原因不生效
    def get_model_perms(self, request):
        model_perms = {
            'add': False,
            'change': self.has_change_permission(request),
            'delete': self.has_delete_permission(request),
            'view': self.has_view_permission(request),
        }
        return model_perms


def flatten_json(df, column_name):
    basic = []
    for i in df[column_name]:
        basic.append(json.loads(i))
    flatten_columns = pd.DataFrame(basic)
    flatten_columns.fillna(0, inplace=True)
    workload_item = list(WorkloadItem.objects.all().values('name', 'weight'))
    workload_item = {i['name']: i['weight'] for i in workload_item}
    for c in flatten_columns.columns:
        flatten_columns[c] = flatten_columns[c] * workload_item[c]
    df = pd.concat([df, flatten_columns], axis=1)
    df = df.drop([column_name], axis=1)
    return df


class WorkloadSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/workload_summary_change_list.html"

    search_fields = ('user__full_name', 'position__name', 'verifier__name', 'remark')
    list_filter = (
        'date', 'user__team__name', 'create_datetime', 'position__name', 'verifier'
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.filter(verify=True).values('user__team__name', 'user__full_name', 'position__name', 'workload'))
        if qs.shape[0] > 0:
            qs.rename(columns={'user__team__name': '组别', 'user__full_name': '姓名', 'position__name': '岗位'}, inplace=True)
            qs = flatten_json(qs, 'workload')
            qs.fillna('0', inplace=True)
            # margins 必须加dropna=False参数才能生效
            qs = pd.pivot_table(qs, index=['组别', '姓名'], values=[c for c in qs.columns if c not in ['组别', '姓名', '岗位']], dropna=False, aggfunc=np.sum, margins=True, margins_name='总计')
            qs.dropna(inplace=True)
            qs['总计'] = qs.sum(axis=1)
            response.context_data['summary'] = qs
        return response


class ManHourItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name', 'weight')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'sale_rule': '当需要设置销量目标并转成分数时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(ManHourItemAdmin, self).get_form(request, obj, **kwargs)


class ManHourRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'man_hour', 'start_datetime', 'end_datetime', 'working_hours', 'output', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    autocomplete_fields = ['user', 'position', 'man_hour', 'verifier', 'verify_user']
    search_fields = ('user__full_name', 'position__name', 'verifier__name')
    fieldsets = (
        ('基本信息', {'fields': ['id', 'user', 'position', 'man_hour', 'start_datetime', 'end_datetime', 'working_hours', 'output', 'verifier', 'verify', 'remark']}),
        ('操作信息', {'fields': ['create_datetime', 'verify_user', 'verify_datetime']}),
    )
    readonly_fields = ('id', 'working_hours', 'output', 'create_datetime', 'verify_user', 'verify_datetime')
    list_filter = (
        'start_datetime', 'create_datetime', 'position__name', 'verifier'
    )

    def working_hours(self, obj):
        return max(round((obj.end_datetime - obj.start_datetime).total_seconds()/3600, 2), 0)
    working_hours.short_description = '工作时长'

    def output(self, obj):
        out = max(round((obj.end_datetime - obj.start_datetime).total_seconds()/3600, 2), 0) * obj.man_hour.weight
        return out
    output.short_description = '折算产出'

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if form.cleaned_data['verify']:
                obj.verify_user = request.user
                obj.verify_datetime = timezone.localtime(timezone.now())
            else:
                obj.verify_user = None
                obj.verify_datetime = None
            super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    # 未知原因不生效
    def get_model_perms(self, request):
        model_perms = {
            'add': False,
            'change': self.has_change_permission(request),
            'delete': self.has_delete_permission(request),
            'view': self.has_view_permission(request),
        }
        return model_perms


class ManHourSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/man_hour_summary_change_list.html"

    search_fields = ('user__full_name', 'position__name', 'man_hour__name', 'verifier__name', 'remark')
    list_filter = (
        'user__team__name', 'create_datetime', 'start_datetime', 'position__name', 'man_hour__name', 'verifier'
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('user__team__name', 'man_hour__name', 'man_hour__weight', 'user__full_name', 'start_datetime', 'end_datetime'))
        if qs.shape[0] > 0:
            qs['working_hours'] = ((qs['end_datetime'] - qs['start_datetime']).dt.total_seconds()/3600).apply(lambda x: max(round(x, 2), 0))
            qs['output'] = qs['working_hours'] * qs['man_hour__weight']
            qs.drop(columns=['start_datetime', 'end_datetime', 'man_hour__weight'], inplace=True)
            qs.rename(columns={'user__team__name': '组别', 'user__full_name': '姓名', 'man_hour__name': '工时项目', 'working_hours': '工作时长', 'output': '产出'}, inplace=True)
            qs = pd.pivot_table(qs, index=['组别', '姓名'], values=['工作时长', '产出'], dropna=False, aggfunc=np.sum, margins=True, margins_name='总计')
            qs.dropna(inplace=True)
            response.context_data['summary'] = qs
        return response


admin.site.register(WorkloadItem, WorkloadItemAdmin)
admin.site.register(WorkloadRecord, WorkloadRecordAdmin)
admin.site.register(WorkloadSummary, WorkloadSummaryAdmin)
admin.site.register(ManHourItem, ManHourItemAdmin)
admin.site.register(ManHourRecord, ManHourRecordAdmin)
admin.site.register(ManHourSummary, ManHourSummaryAdmin)
admin.site.register(Position, PositionAdmin)
