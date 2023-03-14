from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Procurement(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    procurement_code = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project = models.CharField(max_length=256, null=True, blank=True)
    order_code = models.CharField(max_length=64, null=True, blank=True)
    order_type = models.CharField(max_length=128, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    vendor = models.CharField(max_length=256, null=True, blank=True)
    vendor_phone = models.CharField(max_length=32, null=True, blank=True)
    vendor_email = models.CharField(max_length=128, null=True, blank=True)
    vendor_address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_procurement'

    def __str__(self):
        return str(self.id)

class OrderReview(CustomBaseModel):
    issued_by = models.CharField(max_length=128, null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    received_by = models.CharField(max_length=128, null=True, blank=True)
    received_date = models.DateField(null=True, blank=True)
    approved_by = models.CharField(max_length=128, null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)
    acknowledged_by = models.CharField(max_length=128, null=True, blank=True)
    acknowledged_date = models.DateField(null=True, blank=True)
    completed_by = models.CharField(max_length=128, null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_procurement_order_review'

    def __str__(self):
        return str(self.id)

class ProcurementCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_procurement_code_config'

    def __str__(self):
        return str(self.id)