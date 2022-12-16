from django.contrib import admin

from .models import ActiveFiscalYear, FiscalYear, FiscalYearCodeConfig


# Register your models here.

class FiscalYearAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'year_code', 'year_name', 'year_status')

class ActiveFiscalYearAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'year')

class FiscalYearCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(ActiveFiscalYear, ActiveFiscalYearAdmin)
admin.site.register(FiscalYearCodeConfig, FiscalYearCodeConfigAdmin)
