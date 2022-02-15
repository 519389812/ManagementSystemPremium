from django.contrib import admin
from announcement.models import Announcement, AnnouncementRecord, Feedback
import datetime
from io import BytesIO
import pandas as pd
from django.http import HttpResponse
import numpy as np
from user.models import User
from team.models import Team


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "content", "get_to_group", "require_upload",
                    "get_unread_count", "edit_datetime", "url_address", "active")
    list_display_links = ("id", "title",)
    fields = ('title', 'content', 'to_group', 'require_upload', 'deadline', 'author', 'get_to_group',
              'get_to_people', 'get_read_names', 'get_unread_names', 'get_read_count', 'get_unread_count',
              'issue_datetime', 'edit_datetime', 'url_address', "active")  # 设置添加/修改详细信息时，哪些字段显示，在这里 remark 字段将不显示
    readonly_fields = ('author', 'get_to_group', 'get_read_names', 'get_unread_names',
                       'get_read_count', 'get_unread_count', 'issue_datetime', 'edit_datetime',)
    actions = ["export_directly", ]
    search_fields = ("author", "title", "content",)
    date_hierarchy = 'issue_datetime'  # 详细时间分层筛选
    list_filter = ('require_upload', 'active',)
    filter_horizontal = ('team',)  # 设置多对多字段的筛选器

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            try:
                team_id = request.user.team.id
                qs = qs.filter(team__related_parent__iregex=r'\D%s\D' % str(team_id))
            except:
                pass
        return qs

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Get a form Field for a ManyToManyField.
        """
        # db_field.name 本模型下的字段名称
        if db_field.name == "to_group":
            # 过滤
            kwargs["queryset"] = Team.objects.filter(team__in=request.user.team.all())
            # filter_horizontal 保持横向展示
            from django.contrib.admin import widgets
            kwargs['widget'] = widgets.FilteredSelectMultiple(
                db_field.verbose_name,
                db_field.name in self.filter_vertical
            )
        return super(AnnouncementAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_to_group(self, obj):
        return ' '.join([i.name for i in obj.to_group.all()])

    get_to_group.short_description = "阅读组"

    def get_names(self, obj):
        to_group_obj = obj.to_group.all()
        to_people = []
        if len(to_group_obj) != 0:
            for group_obj in to_group_obj:
                group_mamber = [i.full_name for i in group_obj.member.all()]
                to_people += group_mamber
        if len(to_people) != 0:
            to_people = list(set(to_people))
        read_names = AnnouncementRecord.objects.filter(aid=obj.id)
        read_names = list(read_names.values_list("reader", flat=True))
        unread_names = [name for name in to_people if name not in read_names] if len(read_names) != 0 else to_people
        return read_names, unread_names

    # 定义list_display中的自定义方法
    def get_read_count(self, obj):
        read_names, _ = self.get_names(obj)
        return len(read_names)

    get_read_count.short_description = u'已读人数'

    # 定义list_display中的自定义方法
    def get_unread_count(self, obj):
        _, unread_names = self.get_names(obj)
        return len(unread_names)

    get_unread_count.short_description = u'未读人数'

    # 定义read_only_fields中的自定义方法
    def get_read_names(self, obj):
        read_names, _ = self.get_names(obj)
        return ' '.join(read_names)

    get_read_names.short_description = u'已读人员'

    # 定义fields中的自定义方法
    def get_unread_names(self, obj):
        _, unread_names = self.get_names(obj)
        return ' '.join(unread_names)

    get_unread_names.short_description = u'未读人员'

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={'title': '标题', 'content': '内容', 'require_upload': '需要上传',
                                    'deadline': '截止时间', 'author': '作者', 'issue_datetime': '发布时间'})
        data = data[["标题", "内容", "作者", "需要上传", "发布时间", "截止时间"]]
        data['发布时间'] = (data['发布时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
        data['截止时间'] = (data['截止时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
        data = data.sort_values(by=["发布时间"], ascending=True)
        data = data.fillna("")
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format("Export_Directly " + filename + ".xlsx")
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response
    export_directly.short_description = "导出"

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = request.user.get_full_name()
            obj.author = user
            super().save_model(request, obj, form, change)


class AnnouncementRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "announcement", "reader", "read_datetime", "image", "read_status")
    list_display_links = ("id",)
    readonly_fields = ("announcement", "reader", "read_datetime", "image", "read_status")
    actions = ["export_directly", "export_pivot_by_count"]
    search_fields = ("announcement__name", "reader",)
    date_hierarchy = 'read_datetime'  # 详细时间分层筛选
    list_filter = ('read_status',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            try:
                team_id = request.user.team.id
                qs = qs.filter(announcement__team__related_parent__iregex=r'\D%s\D' % str(team_id))
            except:
                pass
        return qs

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={"announcement": '公告', "reader": '阅读人', "read_datetime": '阅读时间'})
        data = data[["公告", "阅读人", "阅读时间"]]
        data['阅读时间'] = (data['阅读时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
        data = data.sort_values(by=["公告", "阅读时间"], ascending=True)
        data = data.fillna("")
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format("Export_Directly " + filename + ".xlsx")
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response
    export_directly.short_description = "直接导出"

    def export_pivot_by_count(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={"announcement": '公告', "reader": '阅读人'})
        data = data[["公告", "阅读人"]]
        data["阅读次数"] = data["阅读人"]
        data = data.fillna("")
        data = pd.pivot_table(data, values=["阅读次数"], index=["阅读人"], aggfunc=np.count_nonzero)
        filename = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(
            "Export_Pivot_By_Count " + filename + ".xlsx")
        data.to_excel(outfile)
        response.write(outfile.getvalue())
        return response
    export_pivot_by_count.short_description = "导出阅读次数统计"


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "announcement", "sender", "sent_datetime", "comment", "reply_to")
    list_display_links = ("id",)
    readonly_fields = ("id", "announcement", "sender", "sent_datetime", "comment", "reply_to")
    search_fields = ("announcement__name", "sender", "comment")
    date_hierarchy = 'sent_datetime'  # 详细时间分层筛选
    actions = ["export_directly"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            try:
                team_id = request.user.team.id
                qs = qs.filter(announcement__team__related_parent__iregex=r'\D%s\D' % str(team_id))
            except:
                pass
        return qs

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={"announcement": '公告', "sender": '评论人', "sent_datetime": '评论时间', "comment": "评论"})
        data = data[["公告", "评论人", "评论时间", "评论"]]
        data['评论时间'] = (data['评论时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
        data = data.sort_values(by=["公告", "评论时间"], ascending=True)
        data = data.fillna("")
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format("Export_Directly " + filename + ".xlsx")
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response
    export_directly.short_description = "直接导出"


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(AnnouncementRecord, AnnouncementRecordAdmin)
admin.site.register(Feedback, FeedbackAdmin)
