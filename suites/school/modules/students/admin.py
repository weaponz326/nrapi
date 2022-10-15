from django.contrib import admin

from .models import Student, StudentCodeConfig


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'student_code')

class StudentCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentCodeConfig, StudentCodeConfigAdmin)
