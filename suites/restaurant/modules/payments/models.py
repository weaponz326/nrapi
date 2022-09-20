from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account
from suites.restaurant.modules.orders.models import Order


# Create your models here.

class Payment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    payment_code = models.CharField(max_length=64, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_payment'
        
    def __str__(self):
        return str(self.id)
