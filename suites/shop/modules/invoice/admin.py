from django.contrib import admin

from .models import Invoice, InvoiceCodeConfig, InvoiceItem


# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'invoice_code', 'invoice_date', 'invoice_status', 'customer_name')

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'invoice', 'product', 'quantity')

class InvoiceCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(InvoiceCodeConfig, InvoiceCodeConfigAdmin)
