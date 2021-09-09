from django.contrib import admin
from user.models import CustomUser, EmailVerifyRecord, QuestionVerifyRecord
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.validators import validate_email


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('个人信息', {'fields': ('first_name', 'last_name', 'full_name', 'email', 'email_verify', 'question', 'answer')}),
        ('团队', {'fields': ('team',)}),
        ('权限', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('其他信息', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'full_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'team')
    list_editable = ('is_active', 'is_staff', 'is_superuser', 'team')
    readonly_fields = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions', )
    autocomplete_fields = ['team']
    search_fields = ('full_name', 'team__name')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not change:
                super().save_model(request, obj, form, change)
            if 'email' in form.cleaned_data.keys():
                if form.cleaned_data['email']:
                    if validate_email(obj.email):
                        messages.error(request, "保存失败，邮箱格式不合法！")
                        messages.set_level(request, messages.ERROR)
                        return
                    email_before = CustomUser.objects.get(id=obj.id).email
                    email_after = form.cleaned_data['email']
                    if email_before != email_after:
                        obj.email_verify = False
            super().save_model(request, obj, form, change)


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'code', 'type', 'close_datetime')


class QuestionVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'close_datetime')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(QuestionVerifyRecord, QuestionVerifyRecordAdmin)

admin.site.site_header = '高端值机管理系统'
admin.site.site_title = '高端值机管理系统'
admin.site.index_title = '高端值机管理系统'
