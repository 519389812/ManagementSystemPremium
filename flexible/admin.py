from django.contrib import admin
from flexible.models import LoadSheet, LoadSheetContent, LoadSheetRecord


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
            'type': '项目为旅客和其他时填写',
            'class_': '项目为旅客和行李时填写',
            'location': '项目为其他时填写',
        }
        kwargs.update({'help_texts': help_texts})
        return super(LoadSheetContentAdmin, self).get_form(request, obj, **kwargs)


class LoadSheetRecordAdmin(admin.ModelAdmin):
    fields = ('user', 'anonymous', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    list_display = ('id', 'user', 'anonymous', 'load_sheet', 'times', 'answer_time', 'score', 'submit_datetime')
    search_fields = ('user__full_name', 'anonymous', 'load_sheet__flight')
    list_filter = ('load_sheet__date',)


admin.site.register(LoadSheet, LoadSheetAdmin)
admin.site.register(LoadSheetContent, LoadSheetContentAdmin)
admin.site.register(LoadSheetRecord, LoadSheetRecordAdmin)
