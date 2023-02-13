from django.contrib import admin
from .models import Admission, AdmissionCodeConfig


# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'patient', 'admission_code', 'admission_date', 'admission_status')

class AdmissionCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Admission, AdmissionAdmin)
admin.site.register(AdmissionCodeConfig, AdmissionCodeConfigAdmin)
