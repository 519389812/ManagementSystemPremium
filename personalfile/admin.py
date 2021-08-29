from django.contrib import admin
from personalfile.models import SkillType, Skill
from team.models import Team
from performance.models import Rule
from performance.admin import return_formfield_for_manytomany, return_formfield_for_foreignkey_rule, return_get_model_perms
from ManagementSystem.admin import return_get_queryset_by_team, return_get_queryset_by_team_regex


class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('team',)
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = return_get_queryset_by_team(request, qs, 'team')
        return qs

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     kwargs = return_formfield_for_foreignkey(request, db_field, kwargs, 'team', Team)
    #     return super(SkillTypeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        kwargs = return_formfield_for_manytomany(self, request, db_field, kwargs, 'team', Team)
        return super(SkillTypeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_model_perms(self, request):
        return return_get_model_perms(self, request)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'score', 'workload', 'bonus', 'rule')
    filter_horizontal = ('team',)
    search_fields = ('name',)
    autocomplete_fields = ['type', 'rule']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = return_get_queryset_by_team(request, qs, 'team')
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs = return_formfield_for_foreignkey_rule(request, db_field, kwargs, 'rule', Rule, 'skill')
        return super(SkillAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        kwargs = return_formfield_for_manytomany(self, request, db_field, kwargs, 'team', Team)
        return super(SkillAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)
