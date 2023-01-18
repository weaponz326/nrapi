from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account
from suites.hotel.modules.rooms.models import Room


# Create your models here.

class Housekeeping(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    housekeeping_code = models.CharField(max_length=64, blank=True)
    housekeeping_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_housekeeping'

    def __str__(self):
        return str(self.id)

class Checklist(CustomBaseModel):
    item_number = models.IntegerField(null=True, blank=True)
    housekeeping = models.ForeignKey(Housekeeping, to_field='id', on_delete=models.DO_NOTHING)
    item_description = models.CharField(max_length=256, null=True, blank=True)
    item_status = models.CharField(max_length=64, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_housekeeping_checklist'

    def __str__(self):
        return str(self.id)

class HousekeepingCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hotel_module_housekeeping_code_config'

    def __str__(self):
        return str(self.id)
