from django.contrib import admin

from .models import Guest, GuestCodeConfig


# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'guest_code', 'guest_name', 'phone')

class GuestCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Guest, GuestAdmin)
admin.site.register(GuestCodeConfig, GuestCodeConfigAdmin)
