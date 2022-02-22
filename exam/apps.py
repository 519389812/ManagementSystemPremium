from django.apps import AppConfig


class ExamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exam'
    verbose_name = '在线测验'
    verbose_name_plural = '在线测验'
