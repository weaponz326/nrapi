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
