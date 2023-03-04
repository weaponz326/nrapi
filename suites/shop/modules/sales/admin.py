from django.contrib import admin

from .models import Sales, SalesCodeConfig


# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'sales_code', 'sales_date', 'quantity')

class SalesCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesCodeConfig, SalesCodeConfigAdmin)
