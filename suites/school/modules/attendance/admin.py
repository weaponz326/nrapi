from django.contrib import admin

from .models import AttendanceCodeConfig, StudentAttendance, StudentAttendanceSheet, TeacherAttendance, TeacherAttendanceSheet


# Register your models here.

class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'attendance_code', 'attendance_name', 'attendance_date', 'clase')

class StudentAttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'attendance')

class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'attendance_code', 'attendance_name', 'attendance_date')

class TeacherAttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'attendance')

class AttendanceCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(StudentAttendance, StudentAttendanceAdmin)
admin.site.register(StudentAttendanceSheet, StudentAttendanceSheetAdmin)
admin.site.register(TeacherAttendance, TeacherAttendanceAdmin)
admin.site.register(TeacherAttendanceSheet, TeacherAttendanceSheetAdmin)
admin.site.register(AttendanceCodeConfig, AttendanceCodeConfigAdmin)
