from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.subjects.models import Subject
from suites.school.modules.teachers.models import Teacher


# Create your models here.

class LessonPlan(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    plan_code = models.CharField(max_length=32, null=True, blank=True)
    plan_name = models.CharField(max_length=256, null=True, blank=True)
    plan_date = models.DateField(null=True, blank=True)
    objectives = models.TextField(null=True, blank=True)
    materials = models.TextField(null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    main_activity = models.TextField(null=True, blank=True)
    closure = models.TextField(null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_lesson_plan'

    def __str__(self):
        return str(self.id)

class LessonPlanCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_lesson_plan_code_config'

    def __str__(self):
        return str(self.id)
