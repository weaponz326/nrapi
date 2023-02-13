from django.contrib import admin
from .models import Bill, BillCodeConfig


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'bill_code')

class BillCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Bill, BillAdmin)
admin.site.register(BillCodeConfig, BillCodeConfigAdmin)
