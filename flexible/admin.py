from django.contrib import admin
from flexible.models import LoadSheet, LoadSheetContent, LoadSheetRecord, LoadSheetRecordSummary
from io import BytesIO
import pandas as pd
import datetime
from django.http import HttpResponse
import numpy as np


class LoadSheetAdmin(admin.ModelAdmin):
    fields = ('flight', 'date', 'stopover', 'destination', 'aircraft', 'passenger', 'baggage', 'SI', 'ACARS', 'EFB', 'description')
    list_display = ('id', 'flight', 'date', 'stopover', 'destination', 'aircraft', 'passenger', 'baggage', 'SI', 'ACARS', 'EFB')
    search_fields = ('flight', 'date', 'destination')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.flight = obj.flight.upper()
            obj.stopover = obj.stopover.upper() if obj.stopover is not None else obj.stopover
            obj.destination = obj.destination.upper()
            obj.aircraft = obj.aircraft.upper()
            obj.SI = obj.SI.upper() if obj.SI is not None else obj.SI
            super().save_model(request, obj, form, change)


class LoadSheetContentAdmin(admin.ModelAdmin):
    fields = ('load_sheet', 'destination', 'project', 'number', 'type', '_class', 'location', 'weight')
    list_display = ('id', 'load_sheet', 'destination', 'project', 'number', 'type', '_class', 'location', 'weight')
    autocomplete_fields = ['load_sheet']
    search_fields = ('load_sheet__flight', 'load_sheet__destination')
    list_filter = ('load_sheet__date',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'type': '项目为旅客和其他时填写',
            '_class': '项目为旅客时填写',
            'location': '项目为行李和其他时填写',
        }
        kwargs.update({'help_texts': help_texts})
        return super(LoadSheetContentAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.destination = obj.destination.upper() if obj.destination is not None else obj.destination
            obj.location = obj.location.upper() if obj.location is not None else obj.location
            super().save_model(request, obj, form, change)


class LoadSheetRecordAdmin(admin.ModelAdmin):
    fields = ('user', 'anonymous', 'anonymous_team', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    list_display = ('id', 'user', 'anonymous', 'anonymous_team', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    search_fields = ('user__full_name', 'anonymous', 'load_sheet__flight')
    list_filter = ('load_sheet__date', 'anonymous_team')
    readonly_fields = ('submit_datetime',)
    actions = ['export_directly', ]  # 导出

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values('id', 'user__full_name', 'anonymous', 'anonymous_team', 'load_sheet__flight', 'times',
                                            'answer_time', 'score', 'submit_datetime'))
        data = data.rename(columns={'id': '序号', 'user__full_name': '用户', 'anonymous': '未登录用户',
                                    'anonymous_team': '未登录用户部门', 'load_sheet__flight': '舱单', 'times': '参与次数',
                                    'answer_time': '答题时长', 'score': '成绩', 'submit_datetime': '提交时间'})
        data = data.fillna('')
        data['提交时间'] = data['提交时间'].dt.tz_convert('Asia/Shanghai')
        data['提交时间'] = data['提交时间'].dt.tz_localize(None)
        filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = "attachment;filename={}".format('LMC Score ' + filename + '.xlsx')
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response
    export_directly.short_description = '导出'


class LoadSheetRecordSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/loadsheet_record_summary_change_list.html"

    search_fields = ('user__full_name', 'anonymous', 'user__team__name', 'anonymous_team')
    list_filter = (
        'user__team__name', 'anonymous', 'user__team__name', 'anonymous_team'
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('load_sheet', 'user__full_name', 'anonymous', 'user__team__name', 'anonymous_team', 'times', 'answer_time', 'score'))
        if qs.shape[0] > 0:
            qs.drop_duplicates(['load_sheet', 'user__full_name', 'anonymous', 'user__team__name', 'anonymous_team'], keep='first', inplace=True)
            qs.rename(columns={'user__full_name': '用户', 'anonymous': '未登录用户', 'user__team__name': '部门', 'anonymous_team': '未登录用户部门', 'score': '得分'}, inplace=True)
            qs.fillna('', inplace=True)
            qs = pd.pivot_table(qs, index=['部门', '未登录用户部门', '用户', '未登录用户'], values=['得分'], dropna=False, aggfunc=np.sum)
            qs.dropna(inplace=True)
            qs = qs.round(2)
            response.context_data['summary'] = qs
        return response


admin.site.register(LoadSheet, LoadSheetAdmin)
admin.site.register(LoadSheetContent, LoadSheetContentAdmin)
admin.site.register(LoadSheetRecord, LoadSheetRecordAdmin)
admin.site.register(LoadSheetRecordSummary, LoadSheetRecordSummaryAdmin)
