from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account


# Create your models here.

class Asset(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    asset_number = models.CharField(max_length=64, null=True, blank=True)
    asset_name = models.CharField(max_length=256, null=True, blank=True)
    category = models.CharField(max_length=128, null=True, blank=True)
    asset_type = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    model = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_purchased = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_asset'

    def __str__(self):
        return str(self.id)
