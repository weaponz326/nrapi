from django.contrib import admin
from .models import Rink


# Register your models here.

class RinkAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'sender', 'recipient', 'rink_type')

admin.site.register(Rink, RinkAdmin)
