from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.classes.models import Clase
from suites.school.modules.students.models import Student
from suites.school.modules.subjects.models import Subject
from suites.school.modules.terms.models import Term


# Create your models here.

class Assessment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    term = models.ForeignKey(Term, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    subject = models.ForeignKey(Subject, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    clase = models.ForeignKey(Clase, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    assessment_code = models.CharField(max_length=32, null=True, blank=True)
    assessment_name = models.CharField(max_length=256, null=True, blank=True)
    assessment_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_assessment'

    def __str__(self):
        return str(self.id)

class AssessmentSheet(CustomBaseModel):
    assessment = models.ForeignKey(Assessment, to_field='id', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, to_field='id', on_delete=models.DO_NOTHING)
    score = models.CharField(max_length=16, blank=True, null=True)
    grade = models.CharField(max_length=8, blank=True, null=True)
    remarks = models.CharField(max_length=256, blank=True, null=True)

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
