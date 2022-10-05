from django.contrib import admin

from .models import Reservation, ReservationCodeConfig


# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'reservation_code', 'reservation_date', 'customer', 'reservation_status')

class ReservationCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationCodeConfig, ReservationCodeConfigAdmin)
