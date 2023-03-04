from django.contrib import admin

from .models import Room


# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'room_number', 'room_type', 'room_status')

admin.site.register(Room, RoomAdmin)
