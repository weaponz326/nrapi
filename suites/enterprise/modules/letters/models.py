from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class SentLetter(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    date_sent = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=64, null=True, blank=True)
    recepient = models.CharField(max_length=126, null=True, blank=True)
    subject = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_letters_sent'

    def __str__(self):
        return str(self.id)

class ReceivedLetter(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    date_received = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=64, null=True, blank=True)
    sender = models.CharField(max_length=126, null=True, blank=True)
    subject = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_letters_received'

    def __str__(self):
        return str(self.id)