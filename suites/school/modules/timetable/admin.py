from django.contrib import admin

from .models import Timetable, TimetableCodeConfig, TimetableClass, TimetablePeriod, TimetableSheet


# Register your models here.

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'timetable_code', 'timetable_name')

class TimetableClassAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'timetable', 'clase')

class TimetablePeriodAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'timetable', 'period', 'period_start', 'period_end')

class TimetableSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'timetable')

class TimetableCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Timetable, TimetableAdmin)
admin.site.register(TimetableClass, TimetableClassAdmin)
admin.site.register(TimetablePeriod, TimetablePeriodAdmin)
admin.site.register(TimetableSheet, TimetableSheetAdmin)
admin.site.register(TimetableCodeConfig, TimetableCodeConfigAdmin)
