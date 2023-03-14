from django.contrib import admin

from .models import Leave, LeaveCodeConfig


# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'leave_code', 'leave_type', 'employee', 'leave_status')

class LeaveCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Leave, LeaveAdmin)
admin.site.register(LeaveCodeConfig, LeaveCodeConfigAdmin)
