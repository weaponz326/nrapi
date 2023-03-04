from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.products.models import Product


# Create your models here.

class Sales(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    sales_code = models.CharField(max_length=32, null=True, blank=True)
    sales_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    invoice_number = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'shop_module_sales'
        
    def __str__(self):
        return str(self.id)

class SalesCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_sales_code_config'

    def __str__(self):
        return str(self.id)
