from django.contrib import admin

from .models import Housekeeping, HousekeepingCodeConfig, Checklist


# Register your models here.

class HousekeepingAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'housekeeping_code', 'housekeeping_date', 'room')

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'item_number', 'item_description', 'item_status')

class HousekeepingCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Housekeeping, HousekeepingAdmin)
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(HousekeepingCodeConfig, HousekeepingCodeConfigAdmin)
