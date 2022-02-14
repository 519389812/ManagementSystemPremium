from django.apps import AppConfig


class NoticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notice'
    verbose_name = '消息管理'
    verbose_name_plural = '消息管理'
