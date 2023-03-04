from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.products.models import Product


# Create your models here.

class Inventory(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    inventory_code = models.CharField(max_length=32, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    refill_ordered = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    container = models.CharField(max_length=128, null=True, blank=True)
    batch_number = models.CharField(max_length=64, null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'shop_module_inventory'
        
    def __str__(self):
        return str(self.id)

class InventoryCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_inventory_code_config'

    def __str__(self):
        return str(self.id)
