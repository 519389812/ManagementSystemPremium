from django.db import models
from user.models import CustomUser


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='发送人')
    submit_datetime = models.DateTimeField(auto_now=True, verbose_name='发送时间')
    comment = models.TextField(max_length=100, verbose_name='内容')
    to_feedback = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='回复')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'

    def __str__(self):
        return self.id

