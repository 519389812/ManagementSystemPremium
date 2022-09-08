from django.contrib import admin
from flexible.models import LoadSheet, LoadSheetContent, LoadSheetRecord
from io import BytesIO
import pandas as pd
import datetime
from django.http import HttpResponse


class LoadSheetAdmin(admin.ModelAdmin):
    fields = ('flight', 'date', 'stopover', 'destination', 'aircraft', 'passenger', 'baggage', 'SI', 'ACARS', 'EFB', 'description')
    list_display = ('id', 'flight', 'date', 'stopover', 'destination', 'aircraft', 'passenger', 'baggage', 'SI', 'ACARS', 'EFB')
    search_fields = ('flight', 'date', 'destination')


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


class LoadSheetRecordAdmin(admin.ModelAdmin):
    fields = ('user', 'anonymous', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    list_display = ('id', 'user', 'anonymous', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    search_fields = ('user__full_name', 'anonymous', 'load_sheet__flight')
    list_filter = ('load_sheet__date',)
    actions = ['export_directly', ]  # 导出

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values('id', 'user__full_name', 'anonymous', 'load_sheet__flight', 'times',
                                            'answer_time', 'score', 'submit_datetime'))
        data = data.rename(columns={'id': '序号', 'user__full_name': '用户', 'anonymous': '未登录用户',
                                    'load_sheet__flight': '舱单', 'times': '参与次数', 'answer_time': '答题时长',
                                    'score': '成绩', 'submit_datetime': '提交时间'})
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


admin.site.register(LoadSheet, LoadSheetAdmin)
admin.site.register(LoadSheetContent, LoadSheetContentAdmin)
admin.site.register(LoadSheetRecord, LoadSheetRecordAdmin)
