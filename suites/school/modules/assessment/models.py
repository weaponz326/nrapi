from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account


# Create your models here.

class Assessment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # subject = models.ForeignKey(Subject, to_field='id', on_delete=models.DO_NOTHING)
    assessment_code = models.CharField(max_length=32, null=True, blank=True)
    assessment_name = models.CharField(max_length=256, null=True, blank=True)
    assessment_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_assessment'

    def __str__(self):
        return str(self.id)

class AssessmentClass(CustomBaseModel):
    assessment = models.ForeignKey(Assessment, to_field='id', on_delete=models.DO_NOTHING)
    # class = models.ForeignKey(Class, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'school_module_assessment_class'

    def __str__(self):
        return str(self.id)

class AssessmentSheet(CustomBaseModel):
    assessment = models.ForeignKey(Assessment, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'school_module_assessment_sheet'

    def __str__(self):
        return str(self.id)

class AssessmentCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_assessment_code_config'

    def __str__(self):
        return str(self.id)
