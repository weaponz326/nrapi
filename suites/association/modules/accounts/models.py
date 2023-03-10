from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account


# Create your models here.

class Account(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    account_name = models.CharField(max_length=126, null=True, blank=True)
    account_number = models.CharField(max_length=64, null=True, blank=True)
    bank_name = models.CharField(max_length=126, null=True, blank=True)
    account_type = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'association_module_account'

    def __str__(self):
        return str(self.id)

class Transaction(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    transaction_date = models.DateTimeField(null=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    transaction_type = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'association_module_account_transaction'
    
    def __str__(self):
        return str(self.id)

class AccountCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'association_module_account_code_config'

    def __str__(self):
        return str(self.id)
