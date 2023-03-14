from django.contrib import admin

from .models import Asset, AssetCodeConfig


# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'asset_number', 'asset_name', 'type', 'status')

class AssetCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetCodeConfig, AssetCodeConfigAdmin)
