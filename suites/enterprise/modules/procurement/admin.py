from django.contrib import admin

from .models import OrderReview, Procurement


# Register your models here.

class ProcurementAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'procurement_code', 'vendor', 'order_code', 'order_type')

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at')

admin.site.register(Procurement, ProcurementAdmin)
admin.site.register(OrderReview, OrderReviewAdmin)
