from django.contrib import admin

from .models import Service, ServiceCodeConfig, ServiceItem


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'service_code', 'service_name', 'service_type', 'guest')

class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'service', 'item_date', 'description', 'amount')

class ServiceCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(ServiceCodeConfig, ServiceCodeConfigAdmin)
