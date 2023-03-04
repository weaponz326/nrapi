from django.contrib import admin

from .models import Receivable, ReceivableCodeConfig


# Register your models here.

class ReceivableAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'receivable_code', 'receivable_date', 'amount', 'customer_name')

class ReceivableCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Receivable, ReceivableAdmin)
admin.site.register(ReceivableCodeConfig, ReceivableCodeConfigAdmin)
