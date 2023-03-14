from django.contrib import admin

from .models import Appraisal, AppraisalCodeConfig, AppraisalSheet


# Register your models here.

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'appraisal_code', 'appraisal_name', 'employee')

class AppraisalSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at')

class AppraisalCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Appraisal, AppraisalAdmin)
admin.site.register(AppraisalSheet, AppraisalSheetAdmin)
admin.site.register(AppraisalCodeConfig, AppraisalCodeConfigAdmin)
