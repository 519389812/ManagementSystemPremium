from django.contrib import admin
from django.utils import timezone


class CompensationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class DowngradeRecordAdmin(admin.ModelAdmin):
    fieldsets = (
        ('基本信息', {'fields': ('id', 'date', 'user', 'service', 'score')}),
        ('其他', {'fields': ('fill_user', 'fill_datetime')})
    )
    list_display = ('id', 'date', 'user', 'service', 'score', 'fill_user', 'fill_datetime')
    # list_editable = ('',)
    # autocomplete_fields = ['',]
    search_fields = ('user__full_name', 'fill_user__full_name',)
    readonly_fields = ('user', 'fill_user', 'fill_datetime')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.fill_user = request.user
            obj.fill_datetime = timezone.localtime(timezone.now())
        super().save_model(request, obj, form, change)
