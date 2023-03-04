from django.contrib import admin

from .models import Purchasing, PurchasingCodeConfig, PurchasingItem


# Register your models here.

class PurchasingAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'purchasing_code', 'purchasing_date', 'purchasing_status', 'supplier')

class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'purchasing', 'product', 'quantity')

class PurchasingCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Purchasing, PurchasingAdmin)
admin.site.register(PurchasingItem, PurchasingItemAdmin)
admin.site.register(PurchasingCodeConfig, PurchasingCodeConfigAdmin)
