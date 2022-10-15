from django.contrib import admin

from .models import Assessment, AssessmentClass, AssessmentCodeConfig, AssessmentSheet


# Register your models here.

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'assessment_code', 'assessment_name', 'assessment_date')

class AssessmentClassAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'assessment')

class AssessmentSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'assessment')

class AssessmentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentClass, AssessmentClassAdmin)
admin.site.register(AssessmentSheet, AssessmentSheetAdmin)
admin.site.register(AssessmentCodeConfig, AssessmentCodeConfigAdmin)
