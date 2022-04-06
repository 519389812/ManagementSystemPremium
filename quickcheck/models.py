from django.db import models
from user.models import CustomUser
from ManagementSystemPremium.safe import aes_encrypt, aes_decrypt
from ManagementSystemPremium.settings import AES_KEY, AES_IV


# 第二种解决储存加密读取解密的方法，自定义field
class CustomEncryptField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(CustomEncryptField, self).__init__(*args, **kwargs)

    # 从数据库读取时的处理
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if value == '':
            return value
        return decrypt_if_not_decrypted(value)

    # 写入数据库时处理
    def to_python(self, value):
        if value is None:
            return value
        if value == '':
            return value
        return encrypt_if_not_encrypted(value)

    # 暂不知何时调用，可以注释；似乎是在储存数据前的二次处理。
    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, EncryptedString):
            return value
        if isinstance(value, DecryptedString):
            return encrypt_if_not_encrypted(value)
        return value


def encrypt_if_not_encrypted(value):
    if isinstance(value, EncryptedString):
        return value
    else:
        value = aes_encrypt(AES_KEY, value, AES_IV)
        return EncryptedString(value)


def decrypt_if_not_decrypted(value):
    if isinstance(value, DecryptedString):
        return value
    else:
        value = aes_decrypt(AES_KEY, value, AES_IV)
        return DecryptedString(value)


class EncryptedString(str):
    pass


class DecryptedString(str):
    pass


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='省份')

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = '省份'

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='city_province', verbose_name='省份')
    name = models.CharField(max_length=300, unique=True, verbose_name='城市')
    summary = CustomEncryptField(max_length=1000, verbose_name='概览')
    policy = CustomEncryptField(max_length=10000, verbose_name='详细政策')
    image = models.ImageField(blank=True, upload_to='quickcheck', verbose_name='图片')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='最新更新时间')
    update_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='最新更新用户')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'
        # ordering = ['province']

    def __str__(self):
        return self.name
