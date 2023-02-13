from django.contrib import admin
from .models import Diagnosis, DiagnosisCodeConfig, DiagnosisReport


# Register your models here.

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'patient', 'diagnosis_code', 'consultant_name')

class DiagnosisReportAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'diagnosis', 'blood_group', 'temperature', 'pulse')

class DiagnosisCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(DiagnosisReport, DiagnosisReportAdmin)
admin.site.register(DiagnosisCodeConfig, DiagnosisCodeConfigAdmin)
