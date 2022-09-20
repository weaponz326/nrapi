from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.orders.models import Order
from modules.customers.models import Customer


# Create your models here.

class Delivery(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    delivery_code = models.CharField(max_length=64, null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_location = models.CharField(max_length=256, null=True, blank=True)
    delivery_status = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_delivery'

    def __str__(self):
        return str(self.id)