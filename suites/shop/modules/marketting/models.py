from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account


# Create your models here.

class Campaign(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    campaign_code = models.CharField(max_length=32, null=True, blank=True)
    campaign_name = models.CharField(max_length=256, null=True, blank=True)
    target_audience = models.TextField(null=True, blank=True)
    campaign_type = models.CharField(max_length=256, null=True, blank=True)
    campaign_status = models.CharField(max_length=64, null=True, blank=True)
    supervisor = models.CharField(max_length=128, null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'shop_module_marketting_campaign'
        
    def __str__(self):
        return str(self.id)

class CampaignCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_marketting_campaign_code_config'

    def __str__(self):
        return str(self.id)
