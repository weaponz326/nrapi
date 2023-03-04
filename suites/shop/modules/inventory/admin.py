from django.contrib import admin

from .models import Inventory, InventoryCodeConfig


# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'inventory_code', 'product', 'stock', 'location')

class InventoryCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryCodeConfig, InventoryCodeConfigAdmin)
