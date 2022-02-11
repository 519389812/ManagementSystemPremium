from django.contrib import admin
from asset.models import Current, Fixed, RoomPurpose, Room, Rack, CurrentStorage, CurrentRecord
from django.contrib import messages
from io import BytesIO
import pandas as pd
import datetime
from django.http import HttpResponse
from django.utils import timezone
from django.utils.html import format_html


class RoomPurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class FixedStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purpose',)
    list_display_links = ('id',)
    search_fields = ('name',)


class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('room__name', 'room__purpose__name')

    def save_model(self, request, obj, form, change):
        if change:
            if 'room' in form.changed_data:
                if len(CurrentStorage.objects.filter(area_name=obj.name)) > 0:
                    messages.success(request, '检查到货架地址有变更，已更新物库存记录')
                    CurrentStorage.objects.filter(area_name=obj.name).update(room_name=obj.room.name)
        super(RackAdmin, self).save_model(request, obj, form, change)


class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')
    list_display_links = ('id',)
    search_fields = ('name',)
    readonly_fields = ['id', 'name', 'quantity']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ['id']
        return self.readonly_fields


class FixedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location',)
    list_display_links = ('id',)
    search_fields = ('name', 'location__name',)


class CurrentRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'current_name', 'quantity', 'in_out', 'area_name', 'expiry_date', 'operation_datetime', 'operation_username', 'comment')
    list_display_links = ('id',)
    search_fields = ('current_name__name', 'quantity', 'in_out', 'area_name__name',)
    fieldsets = (
        ('基本信息', {'fields': ['current_name', 'quantity', 'in_out', 'area_name', 'expiry_date', 'comment']}),
        ('操作信息', {'fields': ['id', 'operation_datetime', 'operation_username']}),
    )
    actions = ['export_directly']
    date_hierarchy = 'operation_datetime'  # 详细时间分层筛选
    list_filter = ('current_name__name', 'in_out', 'area_name__name', 'operation_username',)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['id', 'current_name', 'quantity', 'in_out', 'area_name', 'operation_datetime', 'operation_username']
        else:
            return ['id', 'operation_datetime', 'operation_username']

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={'id': '序号', 'current_name_id': '流动资产名称', 'quantity': '数量',
                                    'in_out': '入出库', 'area_name_id': '位置', 'operation_datetime': '操作时间',
                                    'operation_username': '操作人', 'comment': '备注'})
        data = data[['序号', '流动资产名称', '数量', '入出库', '位置', '操作时间', '操作人', '备注']]
        data['操作时间'] = (data['操作时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
        data = data.sort_values(by=['操作时间'], ascending=True)
        data = data.fillna('')
        filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format('Export_Directly ' + filename + '.xlsx')
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response

    export_directly.short_description = '导出记录'

    def save_model(self, request, obj, form, change):
        try:
            storage_record = CurrentStorage.objects.get(current_name=obj.current_name.name, area_name=obj.area_name,
                                                        expiry_date=obj.expiry_date)
        except:
            storage_record = None
        if storage_record is not None:
            if obj.in_out == 'in':
                storage_record.quantity = storage_record.quantity + obj.quantity
                storage_record.save()
                obj.operation_username = request.user.full_name
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == 'out':
                quantity = storage_record.quantity - obj.quantity
                if quantity < 0:
                    messages.set_level(request, level=messages.ERROR)
                    messages.error(request, '错误！出库数量大于库存数。')
                elif quantity == 0:
                    storage_record.delete()
                    obj.operation_username = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
                else:
                    storage_record.quantity = quantity
                    storage_record.save()
                    obj.operation_username = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
        else:
            if obj.in_out == 'in':
                CurrentStorage.objects.create(current_name=obj.current_name.name, room_name=obj.area_name.room.name,
                                              area_name=obj.area_name.name, quantity=obj.quantity,
                                              expiry_date=obj.expiry_date)
                obj.operation_username = request.user.full_name
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == 'out':
                messages.set_level(request, level=messages.ERROR)
                messages.error(request, '错误！该物资无库存记录。')


class CurrentStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_name', 'room_name', 'area_name', 'quantity', 'expiry_date', 'is_expired')
    search_fields = ('current_name', 'room_name', 'area_name', 'quantity',)
    list_filter = ('current_name', 'room_name', 'area_name', 'quantity',)
    ordering = ('expiry_date', 'current_name')
    actions = ['export_directly']

    def export_directly(self, request, queryset):
        outfile = BytesIO()
        data = pd.DataFrame(queryset.values())
        data = data.rename(columns={'id': '序号', 'current_name': '流动资产名称', 'room_name': '所在房间',
                                    'area_name': '所在位置', 'quantity': '库存', 'expiry_date': '有效期'})
        data = data[['流动资产名称', '所在房间', '所在位置', '库存', '有效期']]
        data = data.sort_values(by=['有效期', '流动资产名称', '所在房间', '所在位置', '库存'], ascending=False)
        data = data.fillna('')
        filename = timezone.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="{}"'.format('Export_Directly ' + filename + '.xlsx')
        data.to_excel(outfile, index=False)
        response.write(outfile.getvalue())
        return response

    export_directly.short_description = '导出记录'

    def is_expired(self, obj):
        if obj.expiry_date is not None:
            expiry_date = obj.expiry_date + datetime.timedelta(hours=8)
            if expiry_date < datetime.date.today():
                ret = '已过期'
                color_code = 'red'
            elif (expiry_date - datetime.date.today()).days <= 30:
                ret = '即将过期'
                color_code = 'orange'
            else:
                ret = '未过期'
                color_code = 'green'
        else:
            ret = '无'
            color_code = 'black'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            ret,
        )

    is_expired.short_description = '是否过期'


admin.site.register(Current, CurrentAdmin)
admin.site.register(Fixed, FixedAdmin)
admin.site.register(RoomPurpose, RoomPurposeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Rack, RackAdmin)


