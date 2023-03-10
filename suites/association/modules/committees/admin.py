from django.contrib import admin

from .models import Committee, CommitteeCodeConfig, CommitteeMember


# Register your models here.

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'committee_name')

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'committee', 'member')

class CommitteeCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(CommitteeCodeConfig, CommitteeCodeConfigAdmin)
