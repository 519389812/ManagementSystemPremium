from django.db import models
from user.models import CustomUser


class RoomPurpose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='用途名称')

    class Meta:
        verbose_name = '设置-房间用途'
        verbose_name_plural = '设置-房间用途'

    def __str__(self):
        return self.name


class FixedStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='状态名称')

    class Meta:
        verbose_name = '设置-固定资产状态'
        verbose_name_plural = '设置-固定资产状态'

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=300, verbose_name='房间编号')
    name = models.CharField(max_length=300, unique=True, verbose_name='房间名称')
    purpose = models.ForeignKey(RoomPurpose, related_name='room_purpose', on_delete=models.CASCADE, verbose_name='用途')

    class Meta:
        verbose_name = '设置-房间'
        verbose_name_plural = '设置-房间'

    def __str__(self):
        return self.name


class CurrentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='流动资产类型')

    class Meta:
        verbose_name = '设置-流动资产类型'
        verbose_name_plural = '设置-流动资产类型'

    def __str__(self):
        return self.name


class Current(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=300, verbose_name='流动资产编号')
    type = models.ForeignKey(CurrentType, related_name='current_type', on_delete=models.CASCADE, verbose_name='类型')
    name = models.CharField(max_length=300, unique=True, verbose_name='流动资产名称')
    unit = models.CharField(max_length=30, verbose_name='单位')

    class Meta:
        verbose_name = '设置-流动资产'
        verbose_name_plural = '设置-流动资产'

    def __str__(self):
        return self.name


class FixedType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, verbose_name='固定资产类型')

    class Meta:
        verbose_name = '设置-固定资产类型'
        verbose_name_plural = '设置-固定资产类型'

    def __str__(self):
        return self.name


class Fixed(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=300, verbose_name='固定资产编号')
    type = models.ForeignKey(FixedType, related_name='fixed_type', on_delete=models.CASCADE, verbose_name='类型')
    name = models.CharField(max_length=300, verbose_name='固定资产名称')
    room = models.ForeignKey(Room, related_name='fixed_room', on_delete=models.CASCADE, verbose_name='位置')
    status = models.ForeignKey(FixedStatus, related_name='fixed_status', on_delete=models.CASCADE, verbose_name='状态')
    expiry_date = models.DateField(blank=True, null=True, verbose_name='过期日期')

    class Meta:
        verbose_name = '设置-固定资产'
        verbose_name_plural = '设置-固定资产'

    def __str__(self):
        return self.name


class Rack(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.OneToOneField(Room, blank=True, null=True, related_name='rack_room', on_delete=models.CASCADE, verbose_name='堆放地')
    fixed = models.OneToOneField(Fixed, blank=True, null=True, related_name='rack_fixed', on_delete=models.CASCADE, verbose_name='堆放货架')

    class Meta:
        verbose_name = '管理-存放位置'
        verbose_name_plural = '管理-存放位置'
        ordering = ['room__name', 'fixed__name']

    def __str__(self):
        return '%s%s' % (self.room.name if self.room else '', self.fixed.name if self.fixed else '')


class CurrentRecord(models.Model):
    id = models.AutoField(primary_key=True)
    current = models.ForeignKey(Current, related_name='currentRecord_current', on_delete=models.CASCADE, verbose_name='流动资产名称')
    quantity = models.PositiveSmallIntegerField(verbose_name='出入库数量')
    rack = models.ForeignKey(Rack, related_name='currentRecord_rack', on_delete=models.CASCADE, verbose_name='位置')
    in_out = models.CharField(max_length=300, choices=(('入库', '入库'), ('出库', '出库')), verbose_name='出入库')
    operating_datetime = models.DateTimeField(auto_now=True, verbose_name='最新操作时间')
    operating_user = models.ForeignKey(CustomUser, related_name='currentRecord_operating_user', on_delete=models.CASCADE, verbose_name='操作人')
    comment = models.TextField(max_length=300, blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '流动资产入出库记录'
        verbose_name_plural = '流动资产入出库记录'

    def __str__(self):
        return self.current.name


class CurrentSummary(CurrentRecord):

    class Meta:
        proxy = True
        verbose_name = '流动资产入出库统计'
        verbose_name_plural = '流动资产入出库统计'


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
