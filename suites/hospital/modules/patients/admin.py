from django.contrib import admin

from .models import Patient, PatientCodeConfig


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'clinical_number')

class PatientCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientCodeConfig, PatientCodeConfigAdmin)
