from django.contrib import admin
from flexible.models import LoadSheet, LoadSheetContent


class LoadSheetAdmin(admin.ModelAdmin):
    fields = ('flight', 'date', 'destination')
    list_display = ('id', 'flight', 'date', 'destination')
    search_fields = ('flight', 'date', 'destination')


class LoadSheetContentAdmin(admin.ModelAdmin):
    fields = ('load_sheet', 'destination', 'project', 'number', 'type', '_class', 'location', 'weight')
    list_display = ('id', 'load_sheet', 'destination', 'project', 'number', 'type', '_class', 'location', 'weight')
    autocomplete_fields = ['load_sheet']
    search_fields = ('load_sheet__flight', 'load_sheet__destination')
    list_filter = ('load_sheet__date',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'type': '项目为行李时无需填写',
            'class_': '项目为旅客时填写',
            'location': '项目为行李和其他时填写',
        }
        kwargs.update({'help_texts': help_texts})
        return super(LoadSheetContentAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(LoadSheet, LoadSheetAdmin)
admin.site.register(LoadSheetContent, LoadSheetContentAdmin)
