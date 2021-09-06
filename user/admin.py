from django.contrib import admin
from user.models import CustomUser, EmailVerifyRecord, QuestionVerifyRecord
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.validators import validate_email


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'full_name', 'email', 'question', 'answer')}),
        ('Team', {'fields': ('team',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'ip_address', 'date_joined')}),
    )
    list_display = ('username', 'full_name', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'team')
    list_editable = ('is_active', 'is_staff', 'is_superuser', 'team')
    readonly_fields = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions', )

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if validate_email(obj.email):
                messages.error(request, "保存失败，邮箱格式不合法！")
                messages.set_level(request, messages.ERROR)
                return
            if not change:
                super().save_model(request, obj, form, change)
            email_before = obj.objects.get(id=obj.id).email
            email_after = form.cleaned_data['email']
            if email_before != email_after and email_after is True:
                obj.email = email_after
                obj.email_verify = False
            super().save_model(request, obj, form, change)


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'code', 'type', 'close_datetime')


class QuestionVerifySourceAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')
    autocomplete_fields = ['user']

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.answer = make_password(obj.answer)
            super().save_model(request, obj, form, change)


class QuestionVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'close_datetime')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(QuestionVerifySource, QuestionVerifySourceAdmin)
admin.site.register(QuestionVerifyRecord, QuestionVerifyRecordAdmin)

admin.site.site_header = '管理系统'
admin.site.site_title = '管理系统'
admin.site.index_title = '管理系统'
