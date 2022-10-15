from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.students.models import Student


# Create your models here.

class Section(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    section_code = models.CharField(max_length=32, null=True, blank=True)
    section_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'school_module_section'

    def __str__(self):
        return str(self.id)

class SectionStudent(CustomBaseModel):
    section = models.ForeignKey(Section, to_field='id', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_section_student'

    def __str__(self):
        return str(self.id)

class SectionCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_section_code_config'

    def __str__(self):
        return str(self.id)
