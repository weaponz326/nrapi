from django.contrib import admin

from .models import Clase, ClassStudent, Department, DepartmentClass


# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'class_name', 'class_abbreviation', 'grade', 'department')

class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'clase', 'student')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'department_name', 'department_head')

class DepartmentClassAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'department', 'clase')

admin.site.register(Clase, ClassAdmin)
admin.site.register(ClassStudent, ClassStudentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentClass, DepartmentClassAdmin)
