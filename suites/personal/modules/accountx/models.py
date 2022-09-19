from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class Account(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    account_name = models.CharField(max_length=126, null=True)
    account_number = models.CharField(max_length=32, null=True)
    bank_name = models.CharField(max_length=126, null=True)
    account_type = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'personal_module_account'

    def __str__(self):
        return str(self.id)

class Transaction(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    transaction_date = models.DateTimeField(null=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    transaction_type = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'personal_module_account_transaction'
    
    def __str__(self):
        return str(self.id)
