from django.contrib import admin
from rule.models import LevelRule, RepeatRule, SaleRule, Position, RewardPenaltyType, RewardPenalty, WorkloadItem


class LevelRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置，则不生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(LevelRuleAdmin, self).get_form(request, obj, **kwargs)


class RepeatRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'day', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置，则不生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RepeatRuleAdmin, self).get_form(request, obj, **kwargs)


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


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
    search_fields = ('name',)


class WorkloadItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name', 'weight')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'sale_rule': '当需要设置销量目标并转成分数时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(WorkloadItemAdmin, self).get_form(request, obj, **kwargs)


class RewardPenaltyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class RewardPenaltyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score', 'repeat_rule')
    search_fields = ('name',)
    autocomplete_fields = ['type', 'repeat_rule']

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'repeat_rule': '当需要设置X天内重复发生某个奖励的规则时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RewardPenaltyAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(LevelRule, LevelRuleAdmin)
admin.site.register(RepeatRule, RepeatRuleAdmin)
admin.site.register(SaleRule, SaleRuleAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(RewardPenaltyType, RewardPenaltyTypeAdmin)
admin.site.register(RewardPenalty, RewardPenaltyAdmin)
admin.site.register(WorkloadItem, WorkloadItemAdmin)
