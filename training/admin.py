from django.contrib import admin
from training.models import TrainingType, Training


class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'training_date', 'expiration_date', 'remind_retraining', 'retraining_period')
    filter_horizontal = ('owner',)
    search_fields = ('name',)
    # autocomplete_fields = ['type', 'owner']


admin.site.register(TrainingType, TrainingTypeAdmin)
admin.site.register(Training, TrainingAdmin)
