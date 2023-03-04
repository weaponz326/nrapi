from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.suppliers.models import Supplier
from suites.shop.modules.products.models import Product


# Create your models here.

class Purchasing(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    purchasing_code = models.CharField(max_length=64, blank=True)
    purchasing_date = models.DateTimeField(null=True, blank=True)
    purchasing_status = models.CharField(max_length=32, null=True, blank=True)
    purchasing_total = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    invoice_number = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'shop_module_purchasing'

    def __str__(self):
        return str(self.id)

class PurchasingItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    purchasing = models.ForeignKey(Purchasing, to_field='id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'shop_module_purchasing_item'

    def __str__(self):
        return str(self.id)

class PurchasingCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_purchasing_code_config'

    def __str__(self):
        return str(self.id)
