from django.contrib import admin

from .models import Asset


# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'asset_number', 'asset_name', 'asset_type', 'status')

admin.site.register(Asset, AssetAdmin)
