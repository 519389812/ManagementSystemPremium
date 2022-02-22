from django.contrib import admin


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'anonymous', 'submit_datetime', 'content', 'contact')
    list_display_links = ('id',)
    readonly_fields = ('id', 'submit_datetime')
    search_fields = ('user__full_name', 'anonymous', 'content')
    list_filter = ('sent_datetime',)
    # date_hierarchy = 'sent_datetime'  # 详细时间分层筛选
    # actions = ['export_directly']

    # def export_directly(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'announcement': '公告', 'sender': '评论人', 'sent_datetime': '评论时间', 'comment': '评论'})
    #     data = data[['公告', '评论人', '评论时间', '评论']]
    #     data['评论时间'] = (data['评论时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    #     data = data.sort_values(by=['公告', '评论时间'], ascending=True)
    #     data = data.fillna('')
    #     filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = "attachment;filename='{}'".format('Export_Directly ' + filename + '.xlsx')
    #     data.to_excel(outfile, index=False)
    #     response.write(outfile.getvalue())
    #     return response
    # export_directly.short_description = '直接导出'
