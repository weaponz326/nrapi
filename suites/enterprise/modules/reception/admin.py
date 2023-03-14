from django.contrib import admin

from .models import VisitCodeConfig, Visit


# Register your models here.

class VisitAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'visit_code', 'visit_date', 'visitor_name', 'visitor_phone')

class VisitCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Visit, VisitAdmin)
admin.site.register(VisitCodeConfig, VisitCodeConfigAdmin)
