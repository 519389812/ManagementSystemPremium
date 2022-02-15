from django.db import models
from user.models import User
from team.models import Team


class DocxInit(models.Model):
    id = models.CharField(max_length=14, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建人")
    template_name = models.CharField(max_length=30, verbose_name="模板名")
    docx_name = models.CharField(max_length=30, verbose_name="文档名")
    content = models.TextField(max_length=500, verbose_name="内容")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")
    version = models.IntegerField(default=0, verbose_name="版本号")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name="最新修改时间")
    close_datetime = models.DateTimeField(blank=True, verbose_name="截止时间")

    class Meta:
        verbose_name = "文档"
        verbose_name_plural = "文档"

    def __str__(self):
        return self.id


class ContentStorage(models.Model):
    id = models.CharField(max_length=29, primary_key=True)
    docx = models.ForeignKey(DocxInit, on_delete=models.CASCADE, verbose_name="模板")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="填写人")
    content = models.TextField(max_length=500, verbose_name="内容")
    signature = models.TextField(max_length=150000, verbose_name="签名", blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name="最新修改时间")

    class Meta:
        verbose_name = "文档内容"
        verbose_name_plural = "文档内容"

    def __str__(self):
        return self.id


class SignatureStorage(models.Model):
    id = models.CharField(max_length=29, primary_key=True)
    docx = models.ForeignKey(DocxInit, on_delete=models.CASCADE, verbose_name="模板")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="填写人")
    content = models.TextField(max_length=500, verbose_name="内容")
    signature = models.TextField(max_length=150000, verbose_name="签名", blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "签名"
        verbose_name_plural = "签名"

    def __str__(self):
        return self.id
