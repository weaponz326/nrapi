from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account
from suites.shop.modules.customers.models import Customer
from suites.shop.modules.products.models import Product


# Create your models here.

class Invoice(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    customer_name = models.CharField(max_length=256, null=True, blank=True)
    customer_contact = models.TextField(null=True, blank=True)
    invoice_code = models.CharField(max_length=64, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    invoice_status = models.CharField(max_length=32, null=True, blank=True)
    invoice_total = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'shop_module_invoice'

    def __str__(self):
        return str(self.id)

class InvoiceItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    invoice = models.ForeignKey(Invoice, to_field='id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'shop_module_invoice_item'

    def __str__(self):
        return str(self.id)

class InvoiceCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_invoice_code_config'

    def __str__(self):
        return str(self.id)
