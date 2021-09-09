from django.db import models
from performance.models import WorkloadRecord


class PersonSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '个人统计'
        verbose_name_plural = '个人统计'
