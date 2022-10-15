from django.contrib import admin

from .models import Subject, SubjectCodeConfig, SubjectTeacher


# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'subject_code', 'subject_name')

class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'subject')

class SubjectCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectTeacher, SubjectTeacherAdmin)
admin.site.register(SubjectCodeConfig, SubjectCodeConfigAdmin)
