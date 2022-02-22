import numpy as np
import pandas as pd
from django.contrib import admin
from exam.models import Course, Question, Exam, ExamRecord

admin.site.register([Course, Question, Exam, ExamRecord])


class AnnouncementRecordSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/exam_summary_change_list.html"

    search_fields = ('user__full_name', 'anonymous', 'exam__title', 'exam__course__name')
    list_filter = ('date',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        # 获取页面传递的筛选参数，并从其他model中查询
        # filters_params = response.context_data['cl'].get_filters_params()
        # filter_string = ''
        # if len(filters_params) > 0:
        #     for k, v in filters_params.items():
        #         filter_string += "%s='%s'," % (k, v)
        #     announcement_queryset = eval('%s.objects.filter(%s)' % (Model, filter_string))
        data = pd.DataFrame(qs.values('user__full_name', 'anonymous', 'exam__id', 'total_score', 'score', 'is_passed'))
        data.fillna('', inplace=True)
        data['is_passed'].str.apply(lambda x: 1 if x is True else 0)
        data['user'] = data['user__full_name'] + data['anonymous']
        data.sort_values(by=['exam__id', 'score'], ascending=False, inplace=True)
        data.drop_duplicates(['exam_id'], keep='first', inplace=True)
        data.drop(columns=['user__full_name', 'anonymous', 'exam__id'])
        data.rename(columns={'user': '姓名', 'total_score': '总分', 'score': '得分', 'is_passed': '通过次数'}, replace=True)
        data = pd.pivot_table(data, columns=['总分', '得分', '总次数', '通过次数'], index=['姓名'], values=['总分', '得分', '总次数', '通过次数'], aggfunc=[np.sum, np.sum, np.count_nonzero, np.sum])
        data['得分率'] = data['得分'] / data['总分']
        data['通过率'] = data['总次数'] / data['通过次数']
        response.context_data['summary'] = data
        return response
