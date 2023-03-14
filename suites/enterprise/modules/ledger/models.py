from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Ledger(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    ledger_code = models.CharField(max_length=64, null=True, blank=True)
    ledger_name = models.CharField(max_length=128, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_ledger'

    def __str__(self):
        return str(self.id)

class LedgerItem(CustomBaseModel):
    ledger = models.ForeignKey(Ledger, to_field='id', on_delete=models.DO_NOTHING)
    item_date = models.DateTimeField(null=True)
    reference_number = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    item_type = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'enterprise_module_ledger_item'
    
    def __str__(self):
        return str(self.id)

class LedgerCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_ledger_code_config'

    def __str__(self):
        return str(self.id)