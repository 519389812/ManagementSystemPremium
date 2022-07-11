from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render, redirect
from ManagementSystemPremium.views import parse_url_param
from django.db.models import Count, Sum
from person.models import SkillType, Skill, Employee, EmployeeSummary
import pandas as pd
import numpy as np
import collections


class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    search_fields = ('name',)
    autocomplete_fields = ['type']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'skills')
    fields = ('id', 'user', 'skill')
    list_display_links = ('id',)
    filter_horizontal = ('skill',)
    search_fields = ('user__full_name',)
    autocomplete_fields = ['user']
    readonly_fields = ('id',)
    list_filter = ('user__team',)

    def skills(self, obj):
        return list(obj.skill.all())
    skills.short_description = '技能'


class EmployeeSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/employee_summary_change_list.html"

    search_fields = ('user__full_name',)
    list_filter = ('user__team',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('user__team__name', 'user__full_name', 'skill__type__name', 'skill__name'))
        if qs.shape[0] > 0:
            qs['skill'] = qs['skill__type__name'] + qs['skill__name']
            qs.drop(columns=['skill__type__name', 'skill__name'], inplace=True)
            qs.rename(columns={'user__team__name': '组别', 'user__full_name': '姓名'}, inplace=True)
            qs['组别'].fillna('-', inplace=True)
            qs = qs.groupby(by=['组别', '姓名']).skill.apply(lambda x: ', '.join(x))
            qs = qs.reset_index(drop=False)
            skill = qs['skill'].str.get_dummies(sep=',')
            qs = pd.concat([qs, skill], axis=1)
            qs['技能数'] = qs.iloc[:, 2:].sum(axis=1)
            qs.drop(columns=['skill'], inplace=True)
            qs.sort_values(by=['组别', '姓名'], inplace=True)
            qs.reset_index(drop=True, inplace=True)
            qs.index = qs.index + 1
            response.context_data['columns'] = qs.columns
            response.context_data['summary'] = qs.values.tolist()
        return response


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeSummary, EmployeeSummaryAdmin)
