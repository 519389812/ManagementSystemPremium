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
    list_display = ('id', 'sn', 'name', 'purpose',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('purpose__name',)
    readonly_fields = ('id',)


class CurrentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'type', 'name')
    list_display_links = ('id',)
    search_fields = ('name', 'type__name')
    list_filter = ('type__name',)
    readonly_fields = ('id',)


class FixedTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)


class FixedAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'name', 'type', 'room', 'status', 'expiry_date', 'is_expired')
    list_display_links = ('id',)
    search_fields = ('name', 'type__name')
    list_editable = ('status',)
    list_filter = ('type__name', 'room__name', 'room__purpose__name', 'status', 'expiry_date')
    readonly_fields = ('id',)

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'expiry_date': '不填写则为长期',
        }
        kwargs.update({'help_texts': help_texts})
        return super(FixedAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            if 'room' in form.changed_data:
                if len(CurrentStorage.objects.filter(rack_name=obj.name)) > 0:
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
            ret = '长期'
            color_code = 'green'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            ret,
        )
    is_expired.short_description = '是否过期'


class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'fixed')
    list_display_links = ('id',)
    search_fields = ('room__name', 'fixed__name')
    list_filter = ('room__name', 'room__purpose__name', 'fixed__name')

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'room': '堆放地和固定资产仅选填一项',
            'fixed': '堆放地和固定资产仅选填一项',
        }
        kwargs.update({'help_texts': help_texts})
        return super(RackAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not form.cleaned_data['room'] and not form.cleaned_data['fixed']:
            messages.set_level(request, level=messages.ERROR)
            messages.error(request, '保存失败！存放地点：堆放地或货架至少填写一项')
        elif form.cleaned_data['room'] and form.cleaned_data['fixed']:
            messages.set_level(request, level=messages.ERROR)
            messages.error(request, '保存失败！存放地点：堆放地或货架仅可填写一项')
        else:
            super(RackAdmin, self).save_model(request, obj, form, change)


class CurrentRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'current', 'quantity', 'rack', 'in_out', 'operating_datetime', 'operating_user', 'comment')
    list_display_links = ('id',)
    search_fields = ('current__name',)
    list_filter = ('rack__room__name', 'rack__fixed__name', 'in_out')
    autocomplete_fields = ('current', 'rack')
    fieldsets = (
        ('基本信息', {'fields': ['id', 'current', 'quantity', 'rack', 'in_out', 'comment']}),
        ('操作信息', {'fields': ['operating_datetime', 'operating_user']}),
    )
    # date_hierarchy = 'operating_datetime'  # 详细时间分层筛选
    readonly_fields = ['id', 'operating_datetime', 'operating_user']

    def save_model(self, request, obj, form, change):
        current_storage = CurrentStorage.objects.filter(current=obj.current, rack=obj.rack)
        if current_storage.count() > 0:
            current_storage = current_storage[0]
            print(3)
            if obj.in_out == '入库':
                print(4)
                current_storage.quantity = current_storage.quantity + obj.quantity
                current_storage.save()
                obj.operating_user = request.user
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == '出库':
                print(5)
                quantity = current_storage.quantity - obj.quantity
                if quantity < 0:
                    messages.set_level(request, level=messages.ERROR)
                    messages.error(request, '错误！出库数量大于库存数。')
                elif quantity == 0:
                    current_storage.delete()
                    obj.operating_user = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
                else:
                    current_storage.quantity = quantity
                    current_storage.save()
                    obj.operating_user = request.user.full_name
                    super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
        else:
            if obj.in_out == '入库':
                obj.operating_user = request.user
                CurrentStorage.objects.create(current=obj.current, rack=obj.rack, quantity=obj.quantity)
                super(CurrentRecordAdmin, self).save_model(request, obj, form, change)
            elif obj.in_out == '出库':
                print(2)
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
    search_fields = ('current', 'rack', 'quantity',)
    list_filter = ('current', 'rack', 'quantity',)
    ordering = ('current',)
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






