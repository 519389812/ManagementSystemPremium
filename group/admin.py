from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from group.models import CustomGroup


class CustomGroupInline(admin.StackedInline):
    model = CustomGroup
    can_delete = False
    verbose_name_plural = '授权组'


class CustomGroupAdmin(GroupAdmin):
    inlines = (CustomGroupInline,)

    # def save_model(self, request, obj, form, change):
    #     if form.is_valid():
    #         group = Group.objects.get(name=obj.name)
    #         # 检查若object无onetoonefield的属性，则表示未创建，则创建
    #         if not hasattr(group, "newgroup"):
    #             NewGroup.objects.create(group=group, team_id=request.user.branch.id)
    #         super().save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # filter表示以newgroup表中的team_id field来筛选
    #     return qs.filter(newgroup__branch_id=request.user.branch.id)


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)
