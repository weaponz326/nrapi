from django.contrib import admin

from .models import LessonPlan, LessonPlanCodeConfig


# Register your models here.

class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'plan_code', 'plan_name', 'plan_date', 'subject', 'teacher')

class LessonPlanCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(LessonPlan, LessonPlanAdmin)
admin.site.register(LessonPlanCodeConfig, LessonPlanCodeConfigAdmin)
