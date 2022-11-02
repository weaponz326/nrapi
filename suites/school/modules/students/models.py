import uuid
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.terms.models import Term


def student_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'school/{}/modules/student/{}'.format(instance.account.id, filename)

# Create your models here.

class Student(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    term = models.ForeignKey(Term, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.FileField(null=True, upload_to=student_upload_path)
    nationality = models.CharField(max_length=64, null=True, blank=True)
    religion = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    post_code = models.CharField(max_length=64, null=True, blank=True)
    student_code = models.CharField(max_length=32, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    previous_school = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'school_module_student'

    def __str__(self):
        return str(self.id)

class StudentCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)
    year_code = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'school_module_student_code_config'

    def __str__(self):
        return str(self.id)
