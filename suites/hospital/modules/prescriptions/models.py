from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.patients.models import Patient


# Create your models here.

class Prescription(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    prescription_code = models.CharField(max_length=64, null=True, blank=True)
    prescription_date = models.DateTimeField(null=True, blank=True)
    consultant_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_prescription'
        
    def __str__(self):
        return str(self.id)

class PrescriptionItem(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    prescription = models.ForeignKey(Prescription, to_field='id', on_delete=models.DO_NOTHING)
    medicine = models.CharField(max_length=256, null=True, blank=True)
    dosage = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_prescription_item'

    def __str__(self):
        return str(self.id)

class PrescriptionCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_prescription_code_config'

    def __str__(self):
        return str(self.id)
