from django.contrib import admin

from .models import AccountUser, Access, Invitation


# Register your models here.

class AccountUserAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'personal_id', 'personal_name', 'access_level')

class AccessAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'admin_access', 'portal_access', 'settings_access')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'invitee', 'invitation_status')

admin.site.register(AccountUser, AccountUserAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Invitation, InvitationAdmin)
