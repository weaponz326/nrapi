from django.contrib import admin

from .models import Bill, BillCodeConfig, CheckinCharge, ServiceCharge


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'bill_code', 'bill_date', 'total_amount')

class CheckinChargeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'bill')

class ServiceChargeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'bill')

class BillCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Bill, BillAdmin)
admin.site.register(CheckinCharge, CheckinChargeAdmin)
admin.site.register(ServiceCharge, ServiceChargeAdmin)
admin.site.register(BillCodeConfig, BillCodeConfigAdmin)
