from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account
from suites.restaurant.modules.customers.models import Customer
from suites.restaurant.modules.tables.models import Table
from suites.restaurant.modules.menu.models import MenuItem


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
    order_total = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'restaurant_module_order'

    def __str__(self):
        return str(self.id)

class OrderItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.DO_NOTHING)
    menu_item = models.ForeignKey(MenuItem, to_field='id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_order_item'

    def __str__(self):
        return str(self.id)

class OrderCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'restaurant_module_order_code_config'

    def __str__(self):
        return str(self.id)
