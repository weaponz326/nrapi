from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.orders.models import Order


# Create your models here.

class Payment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    payment_code = models.CharField(max_length=64, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)
