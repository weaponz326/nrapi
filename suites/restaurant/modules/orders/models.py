from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.customers.models import Customer
from modules.tables.models import Table
from modules.menu.models import MenuItem


# Create your models here.

class Order(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    table = models.ForeignKey(Table, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    customer_name = models.CharField(max_length=256, null=True, blank=True)
    order_code = models.CharField(max_length=64, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    order_type = models.CharField(max_length=64, null=True, blank=True)
    order_status = models.CharField(max_length=32, null=True, blank=True)
    order_total = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(CustomBaseModel):
    order = models.ForeignKey(Order, to_field='id', on_delete=models.DO_NOTHING)
    menu_item = models.ForeignKey(MenuItem, to_field='id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
