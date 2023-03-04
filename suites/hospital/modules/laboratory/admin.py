from django.contrib import admin
from .models import Laboratory, LaboratoryCodeConfig


# Register your models here.

class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'patient', 'lab_code', 'lab_date')

class LaboratoryCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(LaboratoryCodeConfig, LaboratoryCodeConfigAdmin)
