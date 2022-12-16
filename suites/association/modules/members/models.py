import uuid
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account


def member_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'association/{}/modules/member/{}'.format(instance.account.id, filename)

# Create your models here.

class Member(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.FileField(null=True, upload_to=member_upload_path)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    post_code = models.CharField(max_length=64, null=True, blank=True)
    member_code = models.CharField(max_length=32, null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'association_module_member'

    def __str__(self):
        return str(self.id)

class MemberCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)
    year_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'association_module_member_code_config'

    def __str__(self):
        return str(self.id)
