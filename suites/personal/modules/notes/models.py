from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class Note(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    title = models.CharField(null=True, blank=True, max_length=256)
    body = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'personal_module_note'
    def __str__(self):
        return str(self.id)

class NoteCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'personal_module_note_code_config'

    def __str__(self):
        return str(self.id)
