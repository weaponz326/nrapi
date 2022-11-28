from django.contrib import admin

from .models import Group, GroupCodeConfig, GroupMember


# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'group_code', 'group_name')

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'group', 'member')

class GroupCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
admin.site.register(GroupCodeConfig, GroupCodeConfigAdmin)
