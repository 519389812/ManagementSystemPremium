from django.contrib import admin
from flexible.models import LoadSheet, LoadSheetContent


class LoadSheetAdmin(admin.ModelAdmin):
    fields = ('id', 'flight', 'date', 'destination')
    list_display = ('id', 'flight', 'date', 'destination')


class LoadSheetContentAdmin(admin.ModelAdmin):

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
