from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.classes.models import Department
from suites.school.modules.teachers.models import Teacher


# Create your models here.

class Subject(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, to_field='id', on_delete=models.DO_NOTHING, null=True)
    subject_code = models.CharField(max_length=32, null=True, blank=True)
    subject_name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_subject'

    def __str__(self):
        return str(self.id)

class SubjectTeacher(CustomBaseModel):
    subject = models.ForeignKey(Subject, to_field='id', on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_subject_teacher'

    def __str__(self):
        return str(self.id)

class SubjectCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_subject_code_config'

    def __str__(self):
        return str(self.id)
