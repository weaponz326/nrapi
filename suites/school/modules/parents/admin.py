from django.contrib import admin

from .models import Parent, ParentCodeConfig


# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'parent_code', 'first_name', 'last_name', 'phone')

class ParentWardAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'parent', 'ward')

class ParentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Parent, ParentAdmin)
admin.site.register(ParentCodeConfig, ParentCodeConfigAdmin)
