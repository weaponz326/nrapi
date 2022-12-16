from django.contrib import admin

from .models import Leave


# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'leave_code', 'leave_type', 'leave_status')

admin.site.register(Leave, LeaveAdmin)
