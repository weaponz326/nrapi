from django.contrib import admin

from .models import OrderReview, Procurement, ProcurementCodeConfig


# Register your models here.

class ProcurementAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'procurement_code', 'vendor', 'order_code', 'order_type')

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at')

class ProcurementCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Procurement, ProcurementAdmin)
admin.site.register(OrderReview, OrderReviewAdmin)
admin.site.register(ProcurementCodeConfig, ProcurementCodeConfigAdmin)
