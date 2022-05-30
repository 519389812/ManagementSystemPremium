from django.contrib import admin
from downgrade.models import FlightType, Compensation, DowngradeRecord, DowngradeSummary
from django.utils import timezone
from django.db.models import Count, Sum, DateTimeField, DateField, Min, Max, Avg, F, ExpressionWrapper, fields, Value, Func


class FlightTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class CompensationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class DowngradeRecordAdmin(admin.ModelAdmin):
    fieldsets = (
        ('基本信息', {'fields': ('id', 'date', 'type', 'flight_number', 'aircraft_id', 'aircraft')}),
        ('客户信息', {'fields': ('passenger', 'phone', 'ticket', 'release', 'before_class', 'new_class')}),
        ('补偿信息', {'fields': ('compensation', 'compensation_miles', 'compensation_amount')}),
        ('验证信息', {'fields': ('fill_user', 'fill_datetime', 'review', 'review_user', 'review_datetime', 'supervisor_verify', 'supervisor_verify_user', 'supervisor_verify_datetime', 'manager_verify', 'manager_verify_user', 'manager_verify_datetime')})
    )
    list_display = ('id', 'date', 'type', 'flight_number', 'aircraft_id', 'aircraft', 'passenger', 'phone', 'ticket', 'release', 'before_class', 'new_class', 'compensation_miles', 'compensation_amount', 'fill_user', 'fill_datetime', 'review', 'review_user', 'review_datetime', 'supervisor_verify', 'supervisor_verify_user', 'supervisor_verify_datetime', 'manager_verify', 'manager_verify_user', 'manager_verify_datetime')
    # list_editable = ('',)
    # autocomplete_fields = ['',]
    search_fields = ('ticket', 'passenger', 'fill_user__full_name',)
    readonly_fields = ('fill_user', 'fill_datetime', 'review', 'review_user', 'review_datetime', 'supervisor_verify', 'supervisor_verify_user', 'supervisor_verify_datetime', 'manager_verify', 'manager_verify_user', 'manager_verify_datetime')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not any([form.cleaned_data['review'], form.cleaned_data['supervisor_verify'], form.cleaned_data['manager_verify']]):
                obj.fill_user = request.user
                obj.fill_datetime = timezone.localtime(timezone.now())
            if form.cleaned_data['review']:
                obj.review_user = request.user
                obj.review_datetime = timezone.localtime(timezone.now())
            else:
                obj.review_user = None
                obj.review_datetime = None
            if form.cleaned_data['supervisor_verify']:
                obj.supervisor_verify_user = request.user
                obj.supervisor_verify_datetime = timezone.localtime(timezone.now())
            else:
                obj.supervisor_verify_user = None
                obj.supervisor_verify_datetime = None
            if form.cleaned_data['manager_verify']:
                obj.supervisor_verify_user = request.user
                obj.supervisor_verify_datetime = timezone.localtime(timezone.now())
            else:
                obj.manager_verify_user = None
                obj.manager_verify_datetime = None
            super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return True


class DowngradeSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/downgrade_summary_change_list.html"

    search_fields = ('user__team__name', 'user__full_name', 'flight_number')
    list_filter = ('date',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('flight_number'),
            'compensation_miles': Sum('compensation_miles'),
            'compensation_amount': Sum('compensation_amount'),
        }
        data = list(qs.filter(verify=True).values('flight_number').annotate(**metrics).order_by('-compensation_amount'))
        response.context_data['summary'] = data
        return response


admin.site.register(FlightType, FlightTypeAdmin)
admin.site.register(Compensation, CompensationAdmin)
admin.site.register(DowngradeRecord, DowngradeRecordAdmin)
admin.site.register(DowngradeSummary, DowngradeSummaryAdmin)
