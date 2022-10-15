from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.assessment.models import Assessment


# Create your models here.

class Report(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # clase = models.ForeignKey(Clase, to_field='id', on_delete=models.DO_NOTHING)
    report_code = models.CharField(max_length=32, null=True, blank=True)
    report_name = models.CharField(max_length=256, null=True, blank=True)
    report_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_report'

    def __str__(self):
        return str(self.id)

class ReportAssessment(CustomBaseModel):
    report = models.ForeignKey(Report, to_field='id', on_delete=models.DO_NOTHING)
    assessment = models.ForeignKey(Assessment, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_report_assessment'

    def __str__(self):
        return str(self.id)

class ReportSheet(CustomBaseModel):
    report = models.ForeignKey(Report, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_report_sheet'

    def __str__(self):
        return str(self.id)

class ReportCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_report_code_config'

    def __str__(self):
        return str(self.id)
