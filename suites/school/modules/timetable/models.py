from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.classes.models import Clase


# Create your models here.

class Timetable(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    timetable_code = models.CharField(max_length=32, null=True, blank=True)
    timetable_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'school_module_timetable'

    def __str__(self):
        return str(self.id)

class TimetableClass(CustomBaseModel):
    timetable = models.ForeignKey(Timetable, to_field='id', on_delete=models.DO_NOTHING)
    clase = models.ForeignKey(Clase, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_timetable_class'

    def __str__(self):
        return str(self.id)

class TimetablePeriod(CustomBaseModel):
    timetable = models.ForeignKey(Timetable, to_field='id', on_delete=models.DO_NOTHING)
    period = models.CharField(max_length=256, null=True, blank=True)
    period_start = models.TimeField(null=True, blank=True)
    period_end = models.TimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'school_module_timetable_period'

    def __str__(self):
        return str(self.id)

class TimetableSheet(CustomBaseModel):
    timetable = models.ForeignKey(Timetable, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_timetable_sheet'

    def __str__(self):
        return str(self.id)

class TimetableCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_timetable_code_config'

    def __str__(self):
        return str(self.id)
