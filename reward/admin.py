from django.contrib import admin
from reward.models import LevelRule, RepeatRule, RewardPenaltyType, RewardPenalty, RewardPenaltyRecord, RewardPenaltySummary
from django.utils import timezone
from django.db.models import Count, Sum, DateTimeField, DateField, Min, Max, Avg, F, ExpressionWrapper, fields, Value, Func


def get_weight_column(obj, column_name, model_name, model_column):
    return_column = eval('obj.%s.%s' % (model_column, column_name))
    if eval('obj.%s.repeat_rule' % model_column):
        end_date = obj.date
        day_delta = eval('obj.%s.repeat_rule.day' % model_column)
        start_date = end_date - timezone.timedelta(day_delta)
        count = eval('%s.objects.filter(user=obj.user, %s=obj.%s, date__gte=start_date, date__lte=end_date, create_datetime__lt=obj.create_datetime).count()' % (model_name, model_column, model_column))
        if count > 0:
            string = 'obj.%s.repeat_rule.calculation' % model_column
            try:
                return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
            except:
                pass
    if obj.level_rule:
        string = 'obj.level_rule.calculation'
        try:
            return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        except:
            pass
    return return_column


def get_weight_column_value(qs, column_name):
    value_list = []
    for q in qs:
        value_list.append(eval('q.%s' % column_name))
    return value_list


class LevelRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置将无法生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(LevelRuleAdmin, self).get_form(request, obj, **kwargs)


class RepeatRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'day', 'calculation')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'calculation': '应由运算符号和数值组成，如“*2”，若未按规范设置将无法生效',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RepeatRuleAdmin, self).get_form(request, obj, **kwargs)


class RewardPenaltyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class RewardPenaltyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score', 'repeat_rule')
    search_fields = ('name',)
    autocomplete_fields = ['type', 'repeat_rule']

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'repeat_rule': '当需要设置X天内重复发生某个奖励或处罚的规则时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RewardPenaltyAdmin, self).get_form(request, obj, **kwargs)


class RewardPenaltyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'reward_penalty', 'level_rule', 'basic_score', 'weight_score', 'title', 'create_datetime', 'create_user')
    fields = ('id', 'user', 'date', 'reward_penalty', 'level_rule', 'basic_score', 'weight_score', 'title', 'content', 'create_datetime', 'create_user')
    list_display_links = ('id',)
    search_fields = ('user__full_name', 'reward_penalty__name', 'reward_penalty__type__name', 'title', 'content', 'level_rule__name')
    autocomplete_fields = ['user', 'reward_penalty', 'level_rule']
    readonly_fields = ('id', 'score', 'create_datetime', 'create_user', 'basic_score', 'weight_score')
    list_filter = (
        'date', 'user__team', 'reward_penalty__name', 'reward_penalty__type__name', 'level_rule__name'
    )

    # 必须要写入readonly_fields，否则报错
    def basic_score(self, obj):
        return obj.reward_penalty.score
    basic_score.short_description = '基础分数'

    def weight_score(self, obj):
        return get_weight_column(obj, 'score', 'RewardPenaltyRecord', 'reward_penalty')
    weight_score.short_description = '加成后分数'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'level_rule': '同类奖励处罚，因影响的程度不同而加减分不同时，设置此项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RewardPenaltyRecordAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.create_user = request.user
            super().save_model(request, obj, form, change)


class RewardPenaltySummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/reward_penalty_summary_change_list.html"

    search_fields = ('user__full_name', 'reward_penalty__name', 'reward_penalty__type__name', 'title', 'content', 'level_rule__name')
    list_filter = (
        'date', 'user__team', 'reward_penalty__name', 'reward_penalty__type__name',
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        value_list = get_weight_column_value(qs, 'weight_score')
        for i in range(len(qs)):
            RewardPenaltyRecord.objects.filter(id=qs[i].id).update(score=value_list[i])
        metrics = {
            'count': Count('user'),
            'score': Sum('score'),
        }
        data = list(qs.values('user__team__name', 'user__full_name').annotate(**metrics).order_by('-score'))
        response.context_data['summary'] = data
        return response


admin.site.register(LevelRule, LevelRuleAdmin)
admin.site.register(RepeatRule, RepeatRuleAdmin)
admin.site.register(RewardPenaltyType, RewardPenaltyTypeAdmin)
admin.site.register(RewardPenalty, RewardPenaltyAdmin)
admin.site.register(RewardPenaltyRecord, RewardPenaltyRecordAdmin)
admin.site.register(RewardPenaltySummary, RewardPenaltySummaryAdmin)
