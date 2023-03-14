from django.contrib import admin

from .models import Ledger, LedgerCodeConfig, LedgerItem


# Register your models here.

class LedgerAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'ledger_code', 'ledger_name')

class LedgerItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'ledger', 'item_date', 'reference_number', 'item_type', 'amount')

class LedgerCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Ledger, LedgerAdmin)
admin.site.register(LedgerItem, LedgerItemAdmin)
admin.site.register(LedgerCodeConfig, LedgerCodeConfigAdmin)
