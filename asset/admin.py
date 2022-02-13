from django.contrib import admin
from asset.models import RoomPurpose, FixedStatus, CurrentType, Current, FixedType, Fixed, Room, Rack, CurrentStorage, CurrentRecord
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
    list_filter = ('purpose__name',)


class CurrentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    list_display_links = ('id',)
    search_fields = ('name', 'type__name')
    list_filter = ('type__name',)


class FixedTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class FixedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'room', 'status', 'expiry_date', 'is_expired')
    list_display_links = ('id',)
    search_fields = ('name', 'type__name')
    list_editable = ('status',)
    list_filter = ('type__name', 'room__name', 'room__purpose__name', 'status', 'expiry_date', 'is_expired')

    def save_model(self, request, obj, form, change):
        if change:
            if obj.room.id != form.changed_data['room']:
                if len(CurrentStorage.objects.filter(room_name=obj.name)) > 0:
                    messages.success(request, '检查到货架地址有变更，已更新库存记录')
                    CurrentStorage.objects.filter(room_name=obj.name).update(room_name=obj.room.name)
        super(FixedAdmin, self).save_model(request, obj, form, change)

    # 配置过期颜色
    def is_expired(self, obj):
        if obj.expiry_date:
            if obj.expiry_date < datetime.date.today():
                ret = '已过期'
                color_code = 'red'
            elif (obj.expiry_date - datetime.date.today()).days <= 30:
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


class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room', 'fixed')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('room__name', 'room__purpose__name', 'fixed__name')

    def save_model(self, request, obj, form, change):
        if change:
            if not form.changed_data['room'] and not form.changed_data['fixed']:
                messages.set_level(request, level=messages.ERROR)
                messages.error(request, '存放地点：房间或货架至少填写一项')
            else:
                super(RackAdmin, self).save_model(request, obj, form, change)


class CurrentRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'current', 'quantity', 'rack', 'in_out', 'operation_datetime', 'operation_username', 'comment')
    list_display_links = ('id',)
    search_fields = ('current__name',)
    list_filter = ('expiry_date', 'rack__room__name', 'rack__fixed__name', 'in_out')
    autocomplete_fields = ('current', 'rack')
    fieldsets = (
        ('基本信息', {'fields': ['id', 'current', 'quantity', 'rack', 'in_out', 'comment']}),
        ('操作信息', {'fields': ['operation_datetime', 'operation_username']}),
    )
    date_hierarchy = 'operation_datetime'  # 详细时间分层筛选
    readonly_fields = ['operation_datetime', 'operation_username']

    def save_model(self, request, obj, form, change):
        try:
            current_storage = CurrentStorage.objects.get(current=obj.current, rack=obj.rack)
        except:
            current_storage = None
        if current_storage:
            if obj.in_out == 'in':
                current_storage.quantity = current_storage.quantity + obj.quantity
                current_storage.save()
                obj.operation_username = request.user
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == 'out':
                quantity = current_storage.quantity - obj.quantity
                if quantity < 0:
                    messages.set_level(request, level=messages.ERROR)
                    messages.error(request, '错误！出库数量大于库存数。')
                elif quantity == 0:
                    current_storage.delete()
                    obj.operation_username = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
                else:
                    current_storage.quantity = quantity
                    current_storage.save()
                    obj.operation_username = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
        else:
            if obj.in_out == 'in':
                obj.operation_user = request.user
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == 'out':
                messages.set_level(request, level=messages.ERROR)
                messages.error(request, '错误！该物资无库存记录。')

    # 导出功能
    # actions = ['export_directly']
    # def export_directly(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'id': '序号', 'current_name_id': '流动资产名称', 'quantity': '数量',
    #                                 'in_out': '入出库', 'area_name_id': '位置', 'operation_datetime': '操作时间',
    #                                 'operation_username': '操作人', 'comment': '备注'})
    #     data = data[['序号', '流动资产名称', '数量', '入出库', '位置', '操作时间', '操作人', '备注']]
    #     data['操作时间'] = (data['操作时间'] + datetime.timedelta(hours=8)).dt.strftime('%Y-%m-%d %H:%M:%S')
    #     data = data.sort_values(by=['操作时间'], ascending=True)
    #     data = data.fillna('')
    #     filename = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = 'attachment;filename="{}"'.format('Export_Directly ' + filename + '.xlsx')
    #     data.to_excel(outfile, index=False)
    #     response.write(outfile.getvalue())
    #     return response
    # export_directly.short_description = '导出记录'


class CurrentStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'current', 'rack', 'quantity')
    search_fields = ('current_name', 'room_name', 'area_name', 'quantity',)
    list_filter = ('current_name', 'room_name', 'area_name', 'quantity',)
    ordering = ('expiry_date', 'current_name')
    readonly_fields = ['id', 'current', 'rack', 'quantity']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ['id']
        return self.readonly_fields

    # 导出功能
    # actions = ['export_directly']
    # def export_directly(self, request, queryset):
    #     outfile = BytesIO()
    #     data = pd.DataFrame(queryset.values())
    #     data = data.rename(columns={'id': '序号', 'current_name': '流动资产名称', 'room_name': '所在房间',
    #                                 'area_name': '所在位置', 'quantity': '库存', 'expiry_date': '有效期'})
    #     data = data[['流动资产名称', '所在房间', '所在位置', '库存', '有效期']]
    #     data = data.sort_values(by=['有效期', '流动资产名称', '所在房间', '所在位置', '库存'], ascending=False)
    #     data = data.fillna('')
    #     filename = timezone.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    #     response = HttpResponse(content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = 'attachment;filename="{}"'.format('Export_Directly ' + filename + '.xlsx')
    #     data.to_excel(outfile, index=False)
    #     response.write(outfile.getvalue())
    #     return response
    # export_directly.short_description = '导出记录'


admin.site.register(RoomPurpose, RoomPurposeAdmin)
admin.site.register(FixedStatus, FixedStatusAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(CurrentType, CurrentTypeAdmin)
admin.site.register(Current, CurrentAdmin)
admin.site.register(FixedType, FixedTypeAdmin)
admin.site.register(Fixed, FixedAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(CurrentRecord, CurrentRecordAdmin)
admin.site.register(CurrentStorage, CurrentStorageAdmin)






