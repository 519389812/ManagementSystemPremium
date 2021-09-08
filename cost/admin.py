from django.contrib import admin


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score')
    search_fields = ('name',)
    autocomplete_fields = ['type']


class CostRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    fields = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('team__name', 'cost__name', 'create_user__full_name')
    autocomplete_fields = ['team', 'cost', ]
    readonly_fields = ('id', 'create_datetime', 'create_user')
    list_filter = (
        'date', 'team__name', 'cost__name', 'create_user__name',
    )
