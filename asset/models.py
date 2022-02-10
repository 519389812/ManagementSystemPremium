from django.db import models


class RoomPurpose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name="用途名称")

    class Meta:
        verbose_name = '房间用途设置'
        verbose_name_plural = '房间用途设置'

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="房间编号")
    name = models.CharField(max_length=20, unique=True, verbose_name="房间名称")
    purpose = models.ForeignKey(RoomPurpose, related_name='room_purpose', on_delete=models.CASCADE, verbose_name="用途")

    class Meta:
        verbose_name = '房间设置'
        verbose_name_plural = '房间设置'

    def __str__(self):
        return self.name


class Rack(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="货架编号")
    name = models.CharField(max_length=20, unique=True, verbose_name="货架名称")
    room = models.ForeignKey(Room, related_name="room", on_delete=models.DO_NOTHING, verbose_name="所在位置")

    class Meta:
        verbose_name = '管理货架'
        verbose_name_plural = '管理货架'

    def __str__(self):
        return self.name


class Current(models.Model):
    id = models.CharField(max_length=20, primary_key=True, verbose_name="流动资产编号")
    name = models.CharField(max_length=20, unique=True, verbose_name="流动资产名称")

    class Meta:
        verbose_name = '流动资产设置'
        verbose_name_plural = '流动资产设置'

    def __str__(self):
        return self.name


class Fixed(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="固定资产编号")
    name = models.CharField(max_length=20, unique=True, verbose_name="固定资产名称")
    location = models.ForeignKey(Room, on_delete=models.DO_NOTHING, verbose_name="位置")
    status = models.CharField(max_length=6, choices=(("在用", "在用"), ("闲置", "闲置"), ("损坏", "损坏")), verbose_name="状态")

    class Meta:
        verbose_name = '固定资产设置'
        verbose_name_plural = '固定资产设置'

    def __str__(self):
        return self.name


class CurrentRecord(models.Model):
    id = models.AutoField(primary_key=True)
    current_name = models.ForeignKey(Current, to_field="name", related_name="current_name", on_delete=models.DO_NOTHING, verbose_name="名称")
    quantity = models.IntegerField(verbose_name="数量")
    area_name = models.ForeignKey(Rack, to_field="name", related_name="area_name", on_delete=models.DO_NOTHING, verbose_name="所在位置")
    in_out = models.CharField(max_length=6, choices=(("in", "入库"), ("out", "出库")), verbose_name="出入库")
    expiry_date = models.DateTimeField(null=True, verbose_name="有效期")
    operation_datetime = models.DateTimeField(auto_now=True, verbose_name="操作时间")
    operation_username = models.CharField(max_length=16, verbose_name="操作人")
    comment = models.TextField(max_length=200, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "流动资产入出库记录"
        verbose_name_plural = "流动资产入出库记录"

    def __str__(self):
        return self.current_name.name


class CurrentStorage(models.Model):
    id = models.AutoField(primary_key=True)
    current_name = models.CharField(max_length=20, verbose_name="物资名称")
    room_name = models.CharField(max_length=20, verbose_name="所在房间")
    area_name = models.CharField(max_length=20, verbose_name="所在位置")
    quantity = models.IntegerField(verbose_name="库存数量")
    expiry_date = models.DateTimeField(null=True, verbose_name="有效期")

    class Meta:
        verbose_name = "流动资产库存"
        verbose_name_plural = "流动资产库存"

    def __str__(self):
        return self.current_name
