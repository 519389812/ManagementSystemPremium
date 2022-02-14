from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    verbose_name = '服务管理'
    verbose_name_plural = '服务管理'
