from django.contrib import admin
from training.models import CourseType, Course, TrainingRecord
import pandas as pd
import numpy as np


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    search_fields = ('name',)


class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'date', 'expiry_date', 'remind')
    filter_horizontal = ('user',)
    search_fields = ('course__name',)
    list_filter = ('date', 'course__type__name')
    autocomplete_fields = ['course']


class TrainingRecordSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/training_summary_change_list.html"

    list_filter = ('date', 'course__name', 'course__name')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        # 获取页面传递的筛选参数，并从其他model中查询
        # filters_params = response.context_data['cl'].get_filters_params()
        # filter_string = ''
        # if len(filters_params) > 0:
        #     for k, v in filters_params.items():
        #         filter_string += "%s='%s'," % (k, v)
        # qs = eval('Model.objects.filter(%s)' % filter_string)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('course', 'date', 'user'))
        user = qs['user'].str.get_dummies(sep=',')
        qs = pd.concat([qs, user], axis=1)
        qs.drop(columns=['user'], inplace=True)
        qs.sort_values(by=['date'], ascending=True, inplace=True)
        qs.rename(columns={'course': '课程', 'date': '日期'})
        qs = pd.pivot_table(qs, columns=['课程', '日期'])
        response.context_data['columns'] = qs.columns
        response.context_data['summary'] = qs.values.tolist()
        return response


admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TrainingRecord, TrainingRecordAdmin)
