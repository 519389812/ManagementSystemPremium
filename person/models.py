from django.db import models


class PersonSummary:

    class Meta:
        proxy = True
        verbose_name = '个人统计'
        verbose_name_plural = '个人统计'
