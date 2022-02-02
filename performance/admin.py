from django.contrib import admin
from performance.models import Position, WorkloadItem, WorkloadRecord, WorkloadSummary
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


def half_ceil(x):
    return math.modf(x)[1] + (0.5 if math.modf(x)[0] < 0.5 else 1)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
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
    list_display = ('id', 'user', 'date', 'position', 'workload_exchange', 'output', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    autocomplete_fields = ['user', 'position', 'verifier', 'verify_user']
    search_fields = ('user__full_name', 'date', 'position__name', 'verifier__name', 'remark')
    fields = ('id', 'user', 'position', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    readonly_fields = ('id', 'user', 'position', 'workload_exchange', 'output', 'create_datetime', 'verify_user', 'verify_datetime')
    list_filter = (
        'date', 'create_datetime', 'position__name', 'verifier'
    )

    def workload_exchange(self, obj):
        return obj.workload.replace('\"', '').replace('{', '').replace('}', '')
    workload_exchange.short_description = '工作量'

    def output(self, obj):
        workload_item = list(WorkloadItem.objects.filter(position=obj.position).values('name', 'weight'))
        workload_item = {i['name']: i['weight'] for i in workload_item}
        out = sum([v * workload_item[k] for k, v in json.loads(obj.workload).items()])
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


class WorkloadSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/workload_summary_change_list.html"

    search_fields = ('user__full_name', 'position__name', 'verifier__name', 'remark')
    list_filter = (
        'date', 'user__team', 'create_datetime', 'position__name', 'verifier'
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
            'score': Sum('score'),
        }
        data = list(qs.filter(verify=True).values('user__team__name', 'user__full_name').annotate(**metrics).order_by('-score'))
        response.context_data['summary'] = data
        return response


admin.site.register(WorkloadItem, WorkloadItemAdmin)
admin.site.register(WorkloadRecord, WorkloadRecordAdmin)
admin.site.register(WorkloadSummary, WorkloadSummaryAdmin)
admin.site.register(Position, PositionAdmin)
