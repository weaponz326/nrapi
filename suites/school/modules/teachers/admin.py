from django.contrib import admin

from .models import Teacher, TeacherCodeConfig


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'teacher_code')

class TeacherCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherCodeConfig, TeacherCodeConfigAdmin)
