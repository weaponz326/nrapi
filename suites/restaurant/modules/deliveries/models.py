from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account
from suites.restaurant.modules.orders.models import Order


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