from django.contrib import admin

from .models import ExtendedProfile, Invitation


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'gender', 'phone', 'country')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'inviter_id', 'inviter_name', 'inviter_type', 'invitation_status')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
admin.site.register(Invitation, InvitationAdmin)
