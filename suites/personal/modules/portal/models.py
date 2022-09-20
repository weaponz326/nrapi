from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class Rink(CustomBaseModel):
    sender = models.ForeignKey(User, to_field='id', related_name='rink_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, to_field='id', related_name='rink_recipient', on_delete=models.DO_NOTHING)
    rink_type = models.CharField(max_length=64, null=True)
    rink_source = models.CharField(max_length=64, null=True)
    comment = models.TextField(null="True", blank=True)

    class Meta:
        db_table = 'personal_module_portal_rink'

    def __str__(self):
        return str(self.id)
