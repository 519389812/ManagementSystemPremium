from django.db import models
from django.contrib.auth.models import AbstractUser
from team.models import CustomTeam


class CustomUser(AbstractUser):
    ip_address = models.CharField(max_length=20, blank=True, verbose_name="上次登录ip")
    team = models.ForeignKey(CustomTeam, on_delete=models.CASCADE, null=True, blank=True, verbose_name="所属团队")

    def get_full_name(self):
        full_name = '%s%s' % (self.last_name, self.first_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()
    #
    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register', '验证'),
        ('reset', '重设'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户')
    email = models.EmailField(verbose_name="邮箱")
    code = models.CharField(max_length=20, verbose_name='验证码')
    type = models.CharField(choices=send_choices, max_length=10, verbose_name='验证码类型')
    close_datetime = models.DateTimeField(verbose_name='过期时间')

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = '邮箱验证'

    def __str__(self):
        return self.email


class QuestionVerifySource(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户')
    question = models.CharField(max_length=300, verbose_name='密保问题')
    answer = models.CharField(max_length=300, verbose_name='密保答案')

    class Meta:
        verbose_name = '密保问题'
        verbose_name_plural = '密保问题'

    def __str__(self):
        return self.user.username


class QuestionVerifyRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户')
    code = models.CharField(max_length=20, verbose_name='验证码')
    close_datetime = models.DateTimeField(verbose_name='过期时间')

    class Meta:
        verbose_name = '密保问题验证'
        verbose_name_plural = '密保问题验证'

    def __str__(self):
        return self.user.username
