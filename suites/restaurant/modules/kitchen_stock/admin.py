from django.contrib import admin

from .models import StockItem, StockItemCodeConfig


# Register your models here.

class StockItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'item_code', 'item_name', 'quantity')

class StockItemCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(StockItem, StockItemAdmin)
admin.site.register(StockItemCodeConfig, StockItemCodeConfigAdmin)
