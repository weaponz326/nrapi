from django.contrib import admin

from .models import Nurse, NurseCodeConfig


# Register your models here.

class NurseAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'account', 'nurse_code')

class NurseCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix', 'year_code')

admin.site.register(Nurse, NurseAdmin)
admin.site.register(NurseCodeConfig, NurseCodeConfigAdmin)
