from django.db import models
from user.models import CustomUser


class RoomPurpose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='用途名称')

    class Meta:
        verbose_name = '房间用途设置'
        verbose_name_plural = '房间用途设置'

    def __str__(self):
        return self.name


class FixedStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='状态名称')

    class Meta:
        verbose_name = '状态设置'
        verbose_name_plural = '状态设置'

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.CharField(max_length=300, primary_key=True, verbose_name='房间编号')
    name = models.CharField(max_length=300, unique=True, verbose_name='房间名称')
    purpose = models.ForeignKey(RoomPurpose, related_name='room_purpose', on_delete=models.CASCADE, verbose_name='用途')

    class Meta:
        verbose_name = '房间设置'
        verbose_name_plural = '房间设置'

    def __str__(self):
        return self.name


class CurrentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='流动资产类型')

    class Meta:
        verbose_name = '流动资产类型设置'
        verbose_name_plural = '流动资产类型设置'

    def __str__(self):
        return self.name


class Current(models.Model):
    id = models.CharField(max_length=300, primary_key=True, verbose_name='流动资产编号')
    type = models.ForeignKey(CurrentType, related_name='current_type', on_delete=models.CASCADE, verbose_name='类型')
    name = models.CharField(max_length=300, unique=True, verbose_name='流动资产名称')

    class Meta:
        verbose_name = '流动资产设置'
        verbose_name_plural = '流动资产设置'

    def __str__(self):
        return self.name


class FixedType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='固定资产类型')

    class Meta:
        verbose_name = '固定资产类型设置'
        verbose_name_plural = '固定资产类型设置'

    def __str__(self):
        return self.name


class Fixed(models.Model):
    id = models.CharField(max_length=300, primary_key=True, verbose_name='固定资产编号')
    type = models.ForeignKey(FixedType, related_name='fixed_type', on_delete=models.CASCADE, verbose_name='类型')
    name = models.CharField(max_length=300, unique=True, verbose_name='固定资产名称')
    room = models.ForeignKey(Room, related_name='fixed_room', on_delete=models.CASCADE, verbose_name='位置')
    status = models.ForeignKey(FixedStatus, related_name='fixed_status', on_delete=models.CASCADE, verbose_name='状态')
    expiry_date = models.DateField(null=True, verbose_name='过期日期')

    class Meta:
        verbose_name = '固定资产管理'
        verbose_name_plural = '固定资产管理'

    def __str__(self):
        return self.name


class Rack(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.OneToOneField(Room, null=True, related_name='rack_room', on_delete=models.CASCADE, verbose_name='位置')
    fixed = models.OneToOneField(Fixed, null=True, related_name='rack_fixed', on_delete=models.CASCADE, verbose_name='货架对应资产')

    class Meta:
        verbose_name = '管理货架'
        verbose_name_plural = '管理货架'
        ordering = ['room__name', 'fixed__name']

    def __str__(self):
        return self.room__name if self.room__name is not None else self.fixed__name


class CurrentRecord(models.Model):
    id = models.AutoField(primary_key=True)
    current = models.ForeignKey(Current, related_name='currentRecord_current', on_delete=models.CASCADE, verbose_name='流动资产名称')
    quantity = models.FloatField(verbose_name='出入库数量')
    rack = models.ForeignKey(Rack, related_name='currentRecord_rack', on_delete=models.CASCADE, verbose_name='位置')
    in_out = models.CharField(max_length=300, choices=(('入库', '入库'), ('出库', '出库')), verbose_name='出入库')
    operating_datetime = models.DateTimeField(auto_now=True, verbose_name='最新操作时间')
    operating_user = models.ForeignKey(CustomUser, related_name='currentRecord_operating_user', on_delete=models.CASCADE, verbose_name='操作人')
    comment = models.TextField(max_length=300, blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '流动资产入出库记录'
        verbose_name_plural = '流动资产入出库记录'

    def __str__(self):
        return self.current__name


class CurrentStorage(models.Model):
    id = models.AutoField(primary_key=True)
    current = models.ForeignKey(Current, related_name='currentStorage_current', on_delete=models.CASCADE, verbose_name='物资名称')
    rack = models.ForeignKey(Rack, related_name='currentStorage_rack', on_delete=models.CASCADE, verbose_name='所在货架')
    quantity = models.IntegerField(verbose_name='库存数量')

    class Meta:
        verbose_name = '流动资产库存'
        verbose_name_plural = '流动资产库存'

    def __str__(self):
        return self.current.name
