from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Folder(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    folder_number = models.CharField(max_length=64, null=True, blank=True)
    folder_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_files_folder'

    def __str__(self):
        return str(self.id)

class File(CustomBaseModel):
    folder = models.ForeignKey(Folder, to_field='id', on_delete=models.DO_NOTHING)
    file_number = models.CharField(max_length=64, null=True, blank=True)
    file_name = models.CharField(max_length=256, null=True, blank=True)
    file_type = models.CharField(max_length=128, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_file'

    def __str__(self):
        return str(self.id)
