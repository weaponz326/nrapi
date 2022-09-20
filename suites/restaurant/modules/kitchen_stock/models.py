from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account


# Create your models here.

class StockItem(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    item_code = models.CharField(max_length=32, null=True, blank=True)
    item_name = models.CharField(max_length=256, null=True, blank=True)
    category = models.CharField(max_length=128, null=True, blank=True)
    item_type = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    refill_ordered = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_stock_item'
        
    def __str__(self):
        return str(self.id)
