from django.contrib import admin

from .models import Employee, EmployeeCodeConfig


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'employee_code', 'job')

class EmployeeCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeCodeConfig, EmployeeCodeConfigAdmin)
