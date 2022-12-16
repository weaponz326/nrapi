from django.contrib import admin

from .models import Committee, CommitteeMember


# Register your models here.

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'committee_name')

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'committee', 'member')

admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)