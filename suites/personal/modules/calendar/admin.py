from django.contrib import admin

from .models import Calendar, CalendarCodeConfig, Schedule, ScheduleCodeConfig


# Register your models here.

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'calendar_name', 'created_at')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'calendar', 'schedule_name', 'start_date', 'status')

class CalendarCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

class ScheduleCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(CalendarCodeConfig, CalendarCodeConfigAdmin)
admin.site.register(ScheduleCodeConfig, ScheduleCodeConfigAdmin)
