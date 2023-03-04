from django.contrib import admin

from .models import Ward, WardCodeConfig, WardPatient


# Register your models here.

class WardAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'ward_number', 'ward_name', 'ward_type')

class WardPatientAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'ward', 'patient')

class WardCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Ward, WardAdmin)
admin.site.register(WardPatient, WardPatientAdmin)
admin.site.register(WardCodeConfig, WardCodeConfigAdmin)
