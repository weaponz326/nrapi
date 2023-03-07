from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.admissions.models import Admission
from suites.hospital.modules.prescriptions.models import Prescription
from suites.hospital.modules.drugs.models import Drug


# Create your models here.

class Dispense(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admission = models.ForeignKey(Admission, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    prescription = models.ForeignKey(Prescription, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    dispense_code = models.CharField(max_length=64, null=True, blank=True)
    dispense_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_dispensary'
        
    def __str__(self):
        return str(self.id)

class DispenseItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    dispense = models.ForeignKey(Dispense, to_field='id', on_delete=models.DO_NOTHING)
    drug = models.ForeignKey(Drug, to_field='id', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_dispensary_dispense_item'

    def __str__(self):
        return str(self.id)

class DispenseCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_dispensary_dispense_code_config'

    def __str__(self):
        return str(self.id)
