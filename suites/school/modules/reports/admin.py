from django.contrib import admin

from .models import Report, ReportCodeConfig, ReportAssessment


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'report_code', 'report_name', 'report_date', 'clase')

class ReportAssessmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'report', 'assessment')

class ReportCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportAssessment, ReportAssessmentAdmin)
admin.site.register(ReportCodeConfig, ReportCodeConfigAdmin)
