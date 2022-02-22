from django.db import models
from user.models import CustomUser


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=1000, null=True, blank=True, verbose_name='标题')
    content = models.TextField(max_length=100000, verbose_name='内容')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='发送人')
    submit_datetime = models.DateTimeField(auto_now=True, verbose_name='发送时间')
    parent_post = models.ForeignKey('self', null=True, on_delete=models.CASCADE, verbose_name='回复对象')
    related_post = models.JSONField(null=True, blank=True, max_length=300, verbose_name='回复关系')

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return self.content
