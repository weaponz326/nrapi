from django.contrib import admin

from .models import Checkin, CheckinCodeConfig


# Register your models here.

class CheckinAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'checkin_code', 'checkin_date', 'number_nights')

class CheckinCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Checkin, CheckinAdmin)
admin.site.register(CheckinCodeConfig, CheckinCodeConfigAdmin)
