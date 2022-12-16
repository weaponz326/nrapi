from django.contrib import admin

from .models import Assessment, AssessmentCodeConfig, AssessmentSheet


# Register your models here.

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'assessment_code', 'assessment_name', 'assessment_date', 'subject', 'clase')

class AssessmentSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'assessment', 'student', 'score', 'grade')

class AssessmentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentSheet, AssessmentSheetAdmin)
admin.site.register(AssessmentCodeConfig, AssessmentCodeConfigAdmin)
