from django.contrib import admin

from .models import Customer, CustomerCodeConfig


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'customer_code', 'customer_name', 'phone')

class CustomerCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerCodeConfig, CustomerCodeConfigAdmin)
