from django.contrib import admin
from rule.models import SaleRule


class SaleRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'require', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'require': '应由比较符号和数值组成，如“>=5000”，若未按规范设置，则不生效',
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置，则不生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(SaleRuleAdmin, self).get_form(request, obj, **kwargs)



admin.site.register(SaleRule, SaleRuleAdmin)

