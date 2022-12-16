from django.contrib import admin

from .models import Executive


# Register your models here.

class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'member', 'position')

admin.site.register(Executive, ExecutiveAdmin)
