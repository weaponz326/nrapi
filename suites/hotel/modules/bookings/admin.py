from django.contrib import admin

from .models import Booking, BookingCodeConfig, BookedRoom


# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'booking_code', 'booking_date', 'booking_status')

class BookedRoomAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'booking', 'persons_number')

class BookingCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Booking, BookingAdmin)
admin.site.register(BookedRoom, BookedRoomAdmin)
admin.site.register(BookingCodeConfig, BookingCodeConfigAdmin)
