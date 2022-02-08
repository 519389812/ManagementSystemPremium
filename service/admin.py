import numpy as np
from django.contrib import admin
from django.utils import timezone
import pandas as pd


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    fields = ('id', 'name')


class ServiceRecordAdmin(admin.ModelAdmin):
    fields = ('id', 'date', 'user', 'service', 'score', 'fill_user', 'fill_datetime')
    list_display = ('id', 'date', 'user', 'service', 'score', 'fill_user', 'fill_datetime')
    # list_editable = ('',)
    autocomplete_fields = ['user', 'service']
    search_fields = ('user__full_name', 'fill_user__full_name',)
    readonly_fields = ('fill_user', 'fill_datetime')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.fill_user = request.user
            obj.fill_datetime = timezone.localtime(timezone.now())
        super().save_model(request, obj, form, change)


class ServiceRecordSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/service_summary_change_list.html"

    list_filter = ('user__team', 'service')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        qs = pd.DataFrame(qs.values('user__team__name', 'user__full_name', 'score'))
        qs = pd.get_dummies(qs, columns=['score'], prefix='', prefix_sep='')
        qs.rename(columns={'user__team__name': '组别', 'user__full_name': '姓名'})
        pd.pivot_table(qs, index=['组别', '姓名'], aggfunc=np.count_nonzero)
        qs.sort_values(by=['组别', '姓名'])
        response.context_data['columns'] = qs.columns
        response.context_data['summary'] = qs.values.tolist()
        return response