from django.db import models
from user.models import CustomUser
from team.models import CustomTeam


class DocxInit(models.Model):
    id = models.AutoField(primary_key=True)
    docx_id = models.CharField(max_length=30, unique=True, verbose_name="文件id")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="创建人")
    template_name = models.CharField(max_length=30, verbose_name="模板名")
    docx_name = models.CharField(max_length=30, verbose_name="文档名")
    content = models.TextField(max_length=500, verbose_name="内容")
    remote_sign = models.BooleanField(default=False, verbose_name="远程签名")
    team = models.ManyToManyField(CustomTeam, blank=True, verbose_name="目标组")
    version = models.IntegerField(default=0, verbose_name="版本号")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name="最新修改时间")
    close_datetime = models.DateTimeField(blank=True, verbose_name="截止时间")

    class Meta:
        verbose_name = "文档"
        verbose_name_plural = "文档"

    def __str__(self):
        return self.template_name


class ContentStorage(models.Model):
    id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=30, unique=True, verbose_name="文件id")
    docx = models.ForeignKey(DocxInit, on_delete=models.CASCADE, verbose_name="模板")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="填写人")
    content = models.TextField(max_length=500, verbose_name="内容")
    signature_id = models.TextField(max_length=500, verbose_name="签名号")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name="最新修改时间")

    class Meta:
        verbose_name = "文档内容"
        verbose_name_plural = "文档内容"

    def __str__(self):
        return self.content


class SignatureStorage(models.Model):
    id = models.AutoField(primary_key=True)
    signature_id = models.CharField(max_length=30, unique=True, verbose_name="签名id")
    docx = models.ForeignKey(DocxInit, on_delete=models.CASCADE, verbose_name="模板")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="填写人")
    signature = models.TextField(max_length=150000, verbose_name="签名", blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "签名内容"
        verbose_name_plural = "签名内容"

    def __str__(self):
        return self.user.full_name


class SignatureRemoteStorage(models.Model):
    id = models.AutoField(primary_key=True)
    signature_id = models.CharField(max_length=30, unique=True, verbose_name="签名id")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="填写人")
    signature = models.TextField(max_length=150000, verbose_name="签名", blank=True)
    key = models.CharField(max_length=30, verbose_name="密钥")
    is_download = models.BooleanField(default=False, verbose_name="是否下载")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    download_datetime = models.DateTimeField(blank=True, null=True, verbose_name="下载时间")

    class Meta:
        verbose_name = "签名"
        verbose_name_plural = "签名"

    def __str__(self):
        return self.user.full_name
