from django.contrib import admin
from cost.models import CostType, Cost, CostRecord, CostSummary
from django.db.models import Count, Sum


class CostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    search_fields = ('name',)
    autocomplete_fields = ['type']


class CostRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    fields = ('id', 'date', 'team', 'cost', 'quantity', 'remark', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('team__name', 'cost__type__name', 'cost__name', 'create_user__full_name')
    autocomplete_fields = ['team', 'cost']
    readonly_fields = ('id', 'create_datetime', 'create_user')
    list_filter = ('date', 'team__name', 'cost__name')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.create_user = request.user
            super().save_model(request, obj, form, change)


class CostSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/cost_summary_change_list.html"

    search_fields = ('team__name', 'cost__type__name', 'cost__name', 'create_user__full_name')
    list_filter = ('date', )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('team__name'),
            'quantity': Sum('quantity'),
        }
        data = list(qs.values('team__name').annotate(**metrics).order_by('-quantity'))
        response.context_data['summary'] = data
        return response


admin.site.register(CostType, CostTypeAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(CostRecord, CostRecordAdmin)
admin.site.register(CostSummary, CostSummaryAdmin)
