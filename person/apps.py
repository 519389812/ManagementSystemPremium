from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'person'
    verbose_name = '个人技能管理'
    verbose_name_plural = '个人技能管理'
