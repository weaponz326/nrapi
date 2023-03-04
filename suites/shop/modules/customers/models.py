from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account


# Create your models here.

class Customer(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    customer_code = models.CharField(max_length=64, null=True,  blank=True)
    customer_name = models.CharField(max_length=256, null=True,  blank=True)
    customer_type = models.CharField(max_length=256, null=True,  blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    post_code = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        db_table = 'shop_module_customer'
        
    def __str__(self):
        return str(self.id)

class CustomerCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_customer_code_config'

    def __str__(self):
        return str(self.id)
