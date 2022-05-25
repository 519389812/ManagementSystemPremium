from django.contrib import admin
from document.models import DocxInit, ContentStorage, SignatureStorage, SignatureRemoteStorage
from document.docx_handler import *
import json
from ManagementSystemPremium.admin import return_get_queryset_by_parent_team


class DocxInitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "template_name", "docx_name", "content", "remote_sign", "version", "create_datetime", "edit_datetime")
    list_display_links = ("id",)
    filter_horizontal = ("team", )  # 设置多对多字段的筛选器

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = return_get_queryset_by_parent_team(request, qs, "team")
        return qs

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if change:
                obj.version = str(int(obj.version) + 1)
                SignatureStorage.objects.filter(docx__id=obj.id).delete()
            super().save_model(request, obj, form, change)


class ContentStorageAdmin(admin.ModelAdmin):
    list_display = ("id", "docx", "user", "content", "signature_id", "create_datetime", "edit_datetime")
    list_display_links = ("id",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = return_get_queryset_by_parent_team(request, qs, 'docx__team')
        return qs


class SignatureStorageAdmin(admin.ModelAdmin):
    list_display = ("id", "docx", "user", "location", "is_sign", "create_datetime")
    list_display_links = ("id",)

    def is_sign(self, obj):
        if obj.is_confirm:
            return "是"
        else:
            return "是" if obj.signature != "" else ""
    is_sign.short_description = "是否签名"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = return_get_queryset_by_parent_team(request, qs, 'docx__team')
        return qs


class SignatureRemoteStorageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "key", "is_download", "create_datetime")
    list_display_links = ("id",)


admin.site.register(DocxInit, DocxInitAdmin)
admin.site.register(ContentStorage, ContentStorageAdmin)
admin.site.register(SignatureStorage, SignatureStorageAdmin)
admin.site.register(SignatureRemoteStorage, SignatureRemoteStorageAdmin)
