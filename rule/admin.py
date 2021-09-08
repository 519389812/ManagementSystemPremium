from django.contrib import admin
from rule.models import LevelRule, RepeatRule, SaleRule, PositionType, Position, RewardType, Reward, PenaltyType, Penalty


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


class PositionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score', 'sale_rule')
    search_fields = ('name',)
    autocomplete_fields = ['type', 'sale_rule']

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'sale_rule': '当需要设置销量目标并转成分数时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(PositionAdmin, self).get_form(request, obj, **kwargs)


class RewardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class RewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score', 'level_rule', 'repeat_rule')
    search_fields = ('name',)
    autocomplete_fields = ['type', 'level_rule', 'repeat_rule']

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'level_rule': '同类奖励，程度不同加分不同时，设置此项',
            'repeat_rule': '当需要设置X天内重复发生某个奖励的规则时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RewardAdmin, self).get_form(request, obj, **kwargs)


class PenaltyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score', 'level_rule', 'repeat_rule')
    search_fields = ('name',)
    autocomplete_fields = ['type', 'level_rule', 'repeat_rule']

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'level_rule': '同类处罚，程度不同扣分不同时，建议设置程度加成规则',
            'repeat_rule': '当需要设置X天内重复发生某个处罚的规则时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(PenaltyAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(LevelRule, LevelRuleAdmin)
admin.site.register(RepeatRule, RepeatRuleAdmin)
admin.site.register(SaleRule, SaleRuleAdmin)
admin.site.register(PositionType, PositionTypeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(RewardType, RewardTypeAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(PenaltyType, PenaltyTypeAdmin)
admin.site.register(Penalty, PenaltyAdmin)

