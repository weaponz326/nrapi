from django.contrib import admin

from .models import Executive, ExecutiveCodeConfig


# Register your models here.

class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'member', 'position')

class ExecutiveCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(ExecutiveCodeConfig, ExecutiveCodeConfigAdmin)
