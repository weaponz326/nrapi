from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account


# Create your models here.

class Room(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    room_number = models.CharField(max_length=64, null=True,  blank=True)
    room_type = models.CharField(max_length=128, null=True,  blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    rate = models.CharField(max_length=16, null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    room_status = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        db_table = 'hotel_module_room'
        
    def __str__(self):
        return str(self.id)
