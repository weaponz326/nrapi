from django.contrib import admin
from .models import Dispense, DispenseCodeConfig, DispenseItem


# Register your models here.

class DispenseAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'patient', 'dispense_code')

class DispenseItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'dispense')

class DispenseCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Dispense, DispenseAdmin)
admin.site.register(DispenseItem, DispenseItemAdmin)
admin.site.register(DispenseCodeConfig, DispenseCodeConfigAdmin)
