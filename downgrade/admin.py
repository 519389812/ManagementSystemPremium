from django.contrib import admin
from downgrade.models import FlightType, Compensation, DowngradeRecord


class FlightTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class CompensationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class WorkloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'flight_number', 'workload_exchange', 'output', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    list_editable = ('verify',)
    autocomplete_fields = ['user', 'position', 'verifier', 'verify_user']
    search_fields = ('user__full_name', 'date', 'position__name', 'verifier__name', 'remark')
    fields = ('id', 'user', 'position', 'verifier', 'remark', 'create_datetime', 'verify', 'verify_user', 'verify_datetime')
    readonly_fields = ('id', 'user', 'position', 'workload_exchange', 'output', 'create_datetime', 'verify_user', 'verify_datetime')
    list_filter = (
        'date', 'create_datetime', 'position__name', 'verifier'
    )

    def workload_exchange(self, obj):
        return obj.workload.replace('\"', '').replace('{', '').replace('}', '')
    workload_exchange.short_description = '工作量'

    def output(self, obj):
        workload_item = list(WorkloadItem.objects.filter(position=obj.position).values('name', 'weight'))
        workload_item = {i['name']: i['weight'] for i in workload_item}
        out = sum([v * workload_item[k] for k, v in json.loads(obj.workload).items()])
        return out
    output.short_description = '折算收入'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'date': '请以开始工作日期为准!',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadRecordAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if form.cleaned_data['verify']:
                obj.verify_user = request.user
                obj.verify_datetime = timezone.localtime(timezone.now())
            else:
                obj.verify_user = None
                obj.verify_datetime = None
            super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False
