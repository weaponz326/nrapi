from django.db import models

from accounts.models import CustomBaseModel
from accounts.models import Account


# Create your models here.

class Rink(CustomBaseModel):
    sender = models.ForeignKey(Account, to_field='id', related_name='rink_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(Account, to_field='id', related_name='rink_recipient', on_delete=models.DO_NOTHING)
    rink_type = models.CharField(max_length=64, null=True)
    rink_source = models.CharField(max_length=64, null=True)
    comment = models.TextField(null="True", blank=True)

    def __str__(self):
        return str(self.id)
