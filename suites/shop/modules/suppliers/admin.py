from django.contrib import admin

from .models import Supplier, SupplierCodeConfig, SupplierProduct


# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'supplier_code', 'supplier_name', 'phone')

class SupplierProductAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'supplier', 'product')

class SupplierCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierProduct, SupplierProductAdmin)
admin.site.register(SupplierCodeConfig, SupplierCodeConfigAdmin)
