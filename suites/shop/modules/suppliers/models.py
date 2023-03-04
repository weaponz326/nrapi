from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.products.models import Product


# Create your models here.

class Supplier(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    supplier_code = models.CharField(max_length=64, null=True,  blank=True)
    supplier_name = models.CharField(max_length=256, null=True,  blank=True)
    supplier_type = models.CharField(max_length=256, null=True,  blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    post_code = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        db_table = 'shop_module_supplier'
        
    def __str__(self):
        return str(self.id)

class SupplierItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, to_field='id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'shop_module_supplier_item'

    def __str__(self):
        return str(self.id)

class SupplierCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_supplier_code_config'

    def __str__(self):
        return str(self.id)
