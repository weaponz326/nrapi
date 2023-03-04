from django.contrib import admin

from .models import Payable, PayableCodeConfig


# Register your models here.

class PayableAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'payable_code', 'payable_date', 'amount', 'customer_name')

class PayableCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Payable, PayableAdmin)
admin.site.register(PayableCodeConfig, PayableCodeConfigAdmin)
