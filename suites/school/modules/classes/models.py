from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.students.models import Student


# Create your models here.

class Department(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # department_head = models.ForeignKey(Teacher, to_field='id', on_delete=models.DO_NOTHING)
    department_name = models.CharField(max_length=256, null=True, blank=True)
    department_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_department'

    def __str__(self):
        return str(self.id)

class Clase(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, to_field='id', on_delete=models.DO_NOTHING)
    # class_teacher = models.ForeignKey(Teacher, to_field='id', on_delete=models.DO_NOTHING)
    class_name = models.CharField(max_length=256, null=True, blank=True)
    grade = models.CharField(max_length=128, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'school_module_class'

    def __str__(self):
        return str(self.id)

class ClassStudent(CustomBaseModel):
    clase = models.ForeignKey(Clase, to_field='id', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'school_module_class_student'

    def __str__(self):
        return str(self.id)
