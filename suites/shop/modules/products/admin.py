from django.contrib import admin

from .models import Product, ProductCodeConfig


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'product_code', 'product_name', 'price')

class ProductCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCodeConfig, ProductCodeConfigAdmin)
