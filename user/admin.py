from django.contrib import admin
from user.models import CustomUser, EmailVerifyRecord, QuestionVerifyRecord, QuestionVerifySource
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Team', {'fields': ('team',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'ip_address', 'date_joined')}),
    )
    list_display = ('username', 'last_name', 'first_name', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'team')
    list_editable = ('is_active', 'is_staff', 'is_superuser', 'team')
    filter_horizontal = ('groups', 'user_permissions', )


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
