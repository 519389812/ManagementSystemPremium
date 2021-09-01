from django.contrib import admin
from personalfile.models import SkillType, Skill
from team.models import CustomTeam
from performance.models import Rule


class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('team',)
    search_fields = ('name',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'score', 'workload', 'bonus', 'rule')
    filter_horizontal = ('team',)
    search_fields = ('name',)
    autocomplete_fields = ['type', 'rule']


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)
