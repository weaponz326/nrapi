from django.contrib import admin

from .models import AttendanceCodeConfig, Attendance, AttendanceSheet


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'attendance_code', 'attendance_name', 'attendance_date')

class AttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'attendance')

class AttendanceCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceSheet, AttendanceSheetAdmin)
admin.site.register(AttendanceCodeConfig, AttendanceCodeConfigAdmin)
