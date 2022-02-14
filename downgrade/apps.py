from django.apps import AppConfig


class DowngradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'downgrade'
    verbose_name = '降舱管理'
    verbose_name_plural = '降舱管理'
