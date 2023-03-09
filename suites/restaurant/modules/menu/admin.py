from django.contrib import admin

from .models import MenuGroup, MenuGroupCodeConfig, MenuItem, MenuItemCodeConfig


# Register your models here.

class MenuGroupAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'menu_group', 'category')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'menu_group', 'item_code', 'item_name', 'price')

class MenuGroupCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

class MenuItemCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(MenuGroup, MenuGroupAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuGroupCodeConfig, MenuGroupCodeConfigAdmin)
admin.site.register(MenuItemCodeConfig, MenuItemCodeConfigAdmin)
