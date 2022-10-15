import uuid

from django.utils import timezone
from django.db import models

from suites.personal.users.models import CustomBaseModel, User


def accounts_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/{}/accounts/{}'.format(instance.id, filename)

# Create your models here.

class Account(CustomBaseModel):
    creator = models.ForeignKey(User, to_field='id', related_name='school_account', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    about = models.TextField()
    logo = models.FileField(null=True, blank=True, upload_to=accounts_upload_path)

    class Meta:
        db_table = 'school_account'

    def __str__(self):
        return str(self.id)
