from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.customers.models import Customer


# Create your models here.

class Receivable(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    receivable_code = models.CharField(max_length=32, null=True, blank=True)
    receivable_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    invoice_number = models.CharField(max_length=64, null=True, blank=True)
    customer_name = models.CharField(max_length=128, null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'shop_module_receivable'
        
    def __str__(self):
        return str(self.id)

class ReceivableCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_receivable_code_config'

    def __str__(self):
        return str(self.id)
