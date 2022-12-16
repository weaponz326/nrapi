from django.contrib import admin

from .models import Appraisal, AppraisalSheet


# Register your models here.

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'appraisal_code', 'appraisal_name')

class AppraisalSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at')

admin.site.register(Appraisal, AppraisalAdmin)
admin.site.register(AppraisalSheet, AppraisalSheetAdmin)
