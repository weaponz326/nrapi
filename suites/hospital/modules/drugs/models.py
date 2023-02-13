from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.patients.models import Patient


# Create your models here.

class Drug(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    ndc_number = models.CharField(max_length=64, null=True, blank=True)
    drug_name = models.DateTimeField(null=True, blank=True)
    generic_name = models.CharField(max_length=256, null=True, blank=True)
    drug_type = models.CharField(max_length=256, null=True, blank=True)
    unit_dose = models.CharField(max_length=32, null=True, blank=True)
    drug_category = models.CharField(max_length=256, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    batch_number = models.CharField(max_length=64, null=True, blank=True)
    purchased_date = models.DateField(null=True, blank=True)
    initial_quantity = models.IntegerField(null=True, blank=True)
    dispensed_quantity = models.IntegerField(null=True, blank=True)
    remaining_quantity = models.IntegerField(null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    storage_location = models.CharField(max_length=128, null=True, blank=True)
    storage_bin = models.CharField(max_length=128, null=True, blank=True)
    refill_ordered = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_drug'
        
    def __str__(self):
        return str(self.id)

class DrugCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_drug_code_config'

    def __str__(self):
        return str(self.id)
