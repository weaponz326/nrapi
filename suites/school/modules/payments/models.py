from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account


# Create your models here.

class Payment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # bill = models.ForeignKey(Bill, to_field='id', on_delete=models.DO_NOTHING)
    payment_code = models.CharField(max_length=32, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount_paid = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_payment'

    def __str__(self):
        return str(self.id)

class PaymentCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_payment_code_config'

    def __str__(self):
        return str(self.id)
