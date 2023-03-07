from django.contrib import admin
from .models import Prescription, PrescriptionCodeConfig, PrescriptionItem


# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'admission', 'prescription_code')

class PrescriptionItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'prescription', 'medicine')

class PrescriptionCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PrescriptionItem, PrescriptionItemAdmin)
admin.site.register(PrescriptionCodeConfig, PrescriptionCodeConfigAdmin)
