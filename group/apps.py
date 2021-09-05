from django.apps import AppConfig


class GroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'group'
    verbose_name = '用户组'
    verbose_name_plural = '用户组'
