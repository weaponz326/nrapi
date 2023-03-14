from django.contrib import admin

from .models import Account, AccountCodeConfig, Transaction


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'account_name', 'bank_name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'transaction_date', 'transaction_type', 'amount')

class AccountCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(AccountCodeConfig, AccountCodeConfigAdmin)
