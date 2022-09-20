from django.db import models
import uuid

from accounts.models import CustomBaseModel, Account


# Create your models here.

class ExtendedProfile(CustomBaseModel):
    country = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Subscription(CustomBaseModel):
    subscription_type = models.CharField(max_length=30, null=True, blank=True)
    billing_frequency = models.CharField(max_length=30, null=True, blank=True)
    number_users = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return str(self.id)
