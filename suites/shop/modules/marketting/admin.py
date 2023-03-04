from django.contrib import admin

from .models import Campaign, CampaignCodeConfig


# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'campaign_code', 'campaign_name', 'campaign_status', 'start_date')

class CampaignCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CampaignCodeConfig, CampaignCodeConfigAdmin)
