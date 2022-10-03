from django.contrib import admin

from .models import ExtendedProfile, Subscription, SubscriptionEvent


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'email', 'phone', 'country')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'subscription_type', 'billing_frequency', 'number_users')

class SubscriptionEventAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'event', 'amount')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(SubscriptionEvent, SubscriptionEventAdmin)
