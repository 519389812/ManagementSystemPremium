from django.apps import AppConfig


class DocumentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'document'
    verbose_name = '电子签名文档'
    verbose_name_plural = '电子签名文档'
