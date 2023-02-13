from django.contrib import admin
from .models import Drug, DrugCodeConfig


# Register your models here.

class DrugAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'ndc_number', 'drug_name', 'generic_name')

class DrugCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Drug, DrugAdmin)
admin.site.register(DrugCodeConfig, DrugCodeConfigAdmin)
