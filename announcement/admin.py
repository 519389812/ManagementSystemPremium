from django.contrib import admin
from announcement.models import Announcement, AnnouncementRecord, AnnouncementRecordSummary, UploadFile
import datetime
from io import BytesIO
import pandas as pd
from django.http import HttpResponse
import numpy as np
from user.models import CustomUser
from team.models import CustomTeam


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'require_upload', 'get_team', 'get_people', 'get_unread_count',
                    'issue_datetime', 'edit_datetime', 'close_datetime')
    list_display_links = ('id',)
    fieldsets = (
        ('基础信息', {'fields': ('id', 'user', 'title', 'content', 'require_upload', 'close_datetime', 'team', 'people')}),
        ('重复规则', {'fields': ('parent_id', 'repeat', 'repeat_number', 'period_close_datetime')}),
        ('其他', {'fields': ('get_read_names', 'get_read_count', 'get_unread_names', 'get_unread_count', 'issue_datetime', 'edit_datetime')}),
    )
    readonly_fields = ('id', 'user', 'get_team', 'get_people', 'get_read_names', 'get_read_count', 'get_unread_names',
                       'get_unread_count', 'issue_datetime', 'edit_datetime', 'parent_id')
    # actions = ['export_directly', ]  # 导出
    autocomplete_fields = ('user', )
    search_fields = ('title', 'content',)
    # date_hierarchy = 'issue_datetime'  # 详细时间分层筛选
    list_filter = ('issue_datetime', 'require_upload')
    filter_horizontal = ('team', 'people')  # 设置多对多字段的筛选器

    def get_team(self, obj):
        return ' '.join([i.name for i in obj.team.all()])
    get_team.short_description = '阅读组'

    def get_people(self, obj):
        return ' '.join([i.full_name for i in obj.people.all()])
    get_people.short_description = '阅读人员'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            try:
                team_id = request.user.team.id
                qs = qs.filter(team__related_parent__iregex=r'\D%s\D' % str(team_id))
            except:
                pass
        return qs

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     """
    #     Get a form Field for a ManyToManyField.
    #     """
    #     # db_field.name 本模型下的字段名称
    #     if db_field.name == 'team':
    #         # 过滤
    #         kwargs['queryset'] = CustomTeam.objects.filter(team__in=request.user.team.all())
    #         # filter_horizontal 保持横向展示
    #         from django.contrib.admin import widgets
    #         kwargs['widget'] = widgets.FilteredSelectMultiple(
    #             db_field.verbose_name,
    #             db_field.name in self.filter_vertical
    #         )
    #     return super(AnnouncementAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_names(self, obj):
        target_team = obj.team.all()
        target_user = []
        if target_team.count() > 0:
            for team_obj in target_team:
                team_mamber = [i.full_name for i in CustomUser.objects.filter(team=team_obj)]
                target_user += team_mamber
        target_user += obj.people.all().values_list('full_name', flat=True)
        if len(target_user) > 0:
            target_user = list(set(target_user))
        read_names = AnnouncementRecord.objects.filter(announcement=obj)
        read_names = list(read_names.values_list('user__full_name', flat=True))
        unread_names = [name for name in target_user if name not in read_names] if len(read_names) != 0 else target_user
        return read_names, unread_names

    # 定义list_display中的自定义方法
    def get_read_count(self, obj):
        read_names, _ = self.get_names(obj)
        return len(read_names)
    get_read_count.short_description = '已读人数'

    # 定义list_display中的自定义方法
    def get_unread_count(self, obj):
        _, unread_names = self.get_names(obj)
        return len(unread_names)
    get_unread_count.short_description = '未读人数'

    # 定义read_only_fields中的自定义方法
    def get_read_names(self, obj):
        read_names, _ = self.get_names(obj)
        return ' '.join(read_names)
    get_read_names.short_description = '已读人员'

    # 定义fields中的自定义方法
    def get_unread_names(self, obj):
        _, unread_names = self.get_names(obj)
        return ' '.join(unread_names)
    get_unread_names.short_description = '未读人员'

    # def export_directly(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'title': '标题', 'content': '内容', 'require_upload': '需要上传',
    #                                 'deadline': '截止时间', 'author': '作者', 'issue_datetime': '发布时间'})
    #     data = data[['标题', '内容', '作者', '需要上传', '发布时间', '截止时间']]
    #     data['发布时间'] = (data['发布时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    #     data['截止时间'] = (data['截止时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    #     data = data.sort_values(by=['发布时间'], ascending=True)
    #     data = data.fillna('')
    #     filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = "attachment;filename='{}'".format('Export_Directly ' + filename + '.xlsx')
    #     data.to_excel(outfile, index=False)
    #     response.write(outfile.getvalue())
    #     return response
    # export_directly.short_description = '导出'

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.user = request.user
            super(AnnouncementAdmin, self).save_model(request, obj, form, change)


class AnnouncementRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement', 'user', 'read_datetime')
    list_display_links = ('id',)
    readonly_fields = ('announcement', 'user', 'read_datetime')
    # actions = ['export_directly', 'export_pivot_by_count']
    search_fields = ('announcement__user__full_name', 'announcement__title', 'announcement__content')
    # date_hierarchy = 'read_datetime'  # 详细时间分层筛选
    list_filter = ('read_datetime',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            try:
                team_id = request.user.team.id
                qs = qs.filter(announcement__team__related_parent__iregex=r'\D%s\D' % str(team_id))
            except:
                pass
        return qs

    # def export_directly(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'announcement': '公告', 'reader': '阅读人', 'read_datetime': '阅读时间'})
    #     data = data[['公告', '阅读人', '阅读时间']]
    #     data['阅读时间'] = (data['阅读时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    #     data = data.sort_values(by=['公告', '阅读时间'], ascending=True)
    #     data = data.fillna('')
    #     filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = "attachment;filename='{}'".format('Export_Directly ' + filename + '.xlsx')
    #     data.to_excel(outfile, index=False)
    #     response.write(outfile.getvalue())
    #     return response
    # export_directly.short_description = '直接导出'
    #
    # def export_pivot_by_count(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'announcement': '公告', 'reader': '阅读人'})
    #     data = data[['公告', '阅读人']]
    #     data['阅读次数'] = data['阅读人']
    #     data = data.fillna('')
    #     data = pd.pivot_table(data, values=['阅读次数'], index=['阅读人'], aggfunc=np.count_nonzero)
    #     filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = "attachment;filename='{}'".format(
    #         'Export_Pivot_By_Count ' + filename + '.xlsx')
    #     data.to_excel(outfile)
    #     response.write(outfile.getvalue())
    #     return response
    # export_pivot_by_count.short_description = '导出阅读次数统计'


class AnnouncementRecordSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/announcement_summary_change_list.html"

    search_fields = ('user__full_name', 'title', 'content')
    list_filter = ('issue_datetime',)

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
        data = {}
        announcement_record = AnnouncementRecord.objects.all()
        for announcement in qs:
            target_names = list(announcement.people.all().values_list('full_name', flat=True))
            team_name_list = list(announcement.team.all().values_list('name', flat=True))
            for team_name in team_name_list:
                target_user = list(CustomUser.objects.filter(team__name=team_name).values_list('full_name', flat=True))
                target_names += target_user
            read_names = announcement_record.filter(announcement=announcement)
            if read_names.count() > 0:
                read_names = list(set(read_names.values_list('user__full_name', flat=True)))
            else:
                read_names = []
            unread_names = list(set(target_names) - (set(read_names)))  # 集合差集 交集& 并集|
            for name in read_names:
                if data.get(name, '') == '':
                    data.setdefault(name, {'read': 1, 'unread': 0})
                else:
                    data[name]['read'] += 1
            for name in unread_names:
                if data.get(name, '') == '':
                    data.setdefault(name, {'read': 0, 'unread': 1})
                else:
                    data[name]['unread'] += 1
        data = pd.DataFrame(data).T
        data.rename(columns={'read': '已读', 'unread': '未读'}, inplace=True)
        data['总数'] = data['已读'] + data['未读']
        data['阅读率'] = data['已读'] / data['总数']
        data['阅读率'] = data['阅读率'].apply(lambda x: '%.2f%%' % (x*100))
        data.sort_values(['阅读率'], ascending=False, inplace=True)
        response.context_data['summary'] = data
        return response


class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement_record', 'file')
    list_display_links = ('id',)
    search_fields = ('announcement_record__announcement__title', 'announcement_record__announcement__content', 'announcement_record__user__full_name')
    list_filter = ('announcement_record__read_datetime',)


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(AnnouncementRecord, AnnouncementRecordAdmin)
admin.site.register(AnnouncementRecordSummary, AnnouncementRecordSummaryAdmin)
admin.site.register(UploadFile, UploadFileAdmin)
