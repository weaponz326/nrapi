from django.contrib import admin

from .models import Doctor, DoctorCodeConfig


# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'doctor_code')

class DoctorCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorCodeConfig, DoctorCodeConfigAdmin)
