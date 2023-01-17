from django.contrib import admin

from .models import Staff, StaffCodeConfig


# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'staff_code', 'job')

class StaffCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffCodeConfig, StaffCodeConfigAdmin)
