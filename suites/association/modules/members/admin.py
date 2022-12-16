from django.contrib import admin

from .models import Member, MemberCodeConfig


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'member_code')

class MemberCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Member, MemberAdmin)
admin.site.register(MemberCodeConfig, MemberCodeConfigAdmin)
