from django.apps import AppConfig


class FlexibleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flexible'
    verbose_name = '其他应用'
    verbose_name_plural = '其他应用'
