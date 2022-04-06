from django.contrib import admin
from quickcheck.models import Province, City
import os


# 一种解决TextField中显示解密后值的方案，不够灵活
#
# from django.forms import widgets
# from django.db.models import TextField
#
#
# class DecryptWidget(widgets.Textarea):
#
#     def format_value(self, value):
#         try:
#             value = aes_decrypt(AES_KEY, value, AES_IV)
#             # these lines will try to adjust size of TextArea to fit to content
#             # row_lengths = [len(r) for r in value.split('\n')]
#             # self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
#             # self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
#             print(value)
#             return value
#         except Exception as e:
#             return super(DecryptWidget, self).format_value(value)
#
# 在admin中加入
# formfield_overrides = {
#     TextField: {'widget': DecryptWidget}
# }


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'province', 'name', 'summary', 'update_datetime', 'update_user')
    search_fields = ('province__name', 'name')
    readonly_fields = ('update_user', )
    filter = ('update_datetime', )
    ordering = ('province', )

    # 必须要写入readonly_fields，否则报错
    # def basic_score(self, obj):
    #     return obj.reward.score
    # basic_score.short_description = '基础分数'

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {
            'policy': '请按以下格式输入：<br/>*标题1<br/>-正文1...<br/>-正文2...<br/>*标题2<br/>...',
        }
        kwargs.update({'help_texts': help_texts})
        return super(CityAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.update_user = request.user
            if obj.image:
                base, ext = os.path.splitext(obj.image.name)
                obj.image.name = obj.province.name + '_' + obj.name + ext
            super(CityAdmin, self).save_model(request, obj, form, change)


admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
