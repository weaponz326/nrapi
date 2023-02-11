from django.db import models
import uuid

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account


# Create your models here.

class ExtendedProfile(CustomBaseModel):
    country = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_settings_extended_profile'

    def __str__(self):
        return str(self.id)

class Subscription(CustomBaseModel):
    customer_code = models.CharField(max_length=64, null=True, blank=True)
    subscription_code = models.CharField(max_length=64, null=True, blank=True)
    subscription_type = models.CharField(max_length=32, null=True, blank=True)
    billing_frequency = models.CharField(max_length=32, null=True, blank=True)
    number_users = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    plan = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_settings_subscription'

    def __str__(self):
        return str(self.id)

class SubscriptionEvent(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    event = models.CharField(max_length=128, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'hospital_module_settings_subscription_event'

    def __str__(self):
        return str(self.id)
