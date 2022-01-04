from django.contrib import admin
from sale.models import SalesRule
from django.db.models import Count, Sum, DateTimeField, DateField, Min, Max, Avg, F, ExpressionWrapper, fields, Value, Func


class SalesRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'require', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'require': '应由比较符号和数值组成，如“>=5000”，若未按规范设置，则不生效',
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置，则不生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(SalesRuleAdmin, self).get_form(request, obj, **kwargs)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class SalesRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'product', 'flight_number', 'passenger', 'ticket', 'emd', 'destination', 'issue_user', 'amount', 'miles', 'user')
    search_fields = ('product__name', 'flight_number', 'passenger', 'ticket', 'emd', 'destination', 'user__full_name', 'issue_user__full_name')
    list_filter = ('date', 'user__team')


class SalesSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/sales_summary_change_list.html"

    search_fields = ('product__name', 'flight_number', 'passenger', 'ticket', 'emd', 'destination', 'user__full_name', 'issue_user__full_name')
    list_filter = ('date', 'user__team', 'create_datetime', 'position__name', 'verifier')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'amount': Sum('amount'),
            'miles': Sum('miles'),
            'total': Sum('amount') + Sum('score')/20,
        }
        data = list(qs.filter(verify=True).values('user__team__name', 'user__full_name').annotate(**metrics).order_by('-score'))
        response.context_data['summary'] = data
        return response


admin.site.register(SalesRule, SalesRuleAdmin)
admin.site.register(SalesRule, SalesRuleAdmin)
admin.site.register(SalesRule, SalesRuleAdmin)
