from django.contrib import admin
from rule.models import PositionType, Position, RewardType, Reward, PenaltyType, Penalty


class PositionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score')
    search_fields = ('name',)


class RewardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class RewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score')
    search_fields = ('name',)
    # autocomplete_fields = ['type']


class PenaltyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'score')
    search_fields = ('name',)
    # autocomplete_fields = ['type']


admin.site.register(PositionType, PositionTypeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(RewardType, RewardTypeAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(PenaltyType, PenaltyTypeAdmin)
admin.site.register(Penalty, PenaltyAdmin)

