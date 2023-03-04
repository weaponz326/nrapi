from django.contrib import admin
from .models import Payment, PaymentCodeConfig


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'payment_code', 'amount_paid', 'order')

class PaymentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentCodeConfig, PaymentCodeConfigAdmin)
