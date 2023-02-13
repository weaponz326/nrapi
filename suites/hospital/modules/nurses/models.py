import uuid
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account


def nurse_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'hospital/{}/modules/nurse/{}'.format(instance.account.id, filename)

# Create your models here.

class Nurse(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.FileField(null=True, upload_to=nurse_upload_path)
    nationality = models.CharField(max_length=64, null=True, blank=True)
    religion = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    post_code = models.CharField(max_length=64, null=True, blank=True)
    nurse_code = models.CharField(max_length=32, null=True, blank=True)
    department = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_nurse'

    def __str__(self):
        return str(self.id)

class NurseCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)
    year_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_nurse_code_config'

    def __str__(self):
        return str(self.id)
