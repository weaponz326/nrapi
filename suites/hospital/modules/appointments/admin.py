from django.contrib import admin
from .models import Appointment, AppointmentCodeConfig


# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'patient', 'appointment_code', 'appointment_status')

class AppointmentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AppointmentCodeConfig, AppointmentCodeConfigAdmin)
