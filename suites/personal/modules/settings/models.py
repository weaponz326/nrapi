from django.db import models

from users.models import CustomBaseModel
from users.models import User


# Create your models here.

class ExtendedProfile(CustomBaseModel):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=16, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

class Invitation(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    invitation_status = models.CharField(max_length=16, null=True, blank=True)
    inviter_type = models.CharField(max_length=32, null=True, blank=True)
    inviter_invitation_id = models.CharField(max_length=64, null=True, blank=True)
    inviter_id = models.CharField(max_length=64, null=True, blank=True)
    inviter_name = models.CharField(max_length=256, null=True, blank=True)
    inviter_location = models.CharField(max_length=256, null=True, blank=True)
