from django.db import models
from user.models import CustomUser


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, verbose_name='登录用户')
    anonymous = models.CharField(max_length=300, null=True, blank=True, verbose_name='未登录用户')
    submit_datetime = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    content = models.TextField(max_length=100000, verbose_name='内容')
    contact = models.TextField(max_length=1000, null=True, blank=True, verbose_name='联系方式')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'

    def __str__(self):
        return self.content

