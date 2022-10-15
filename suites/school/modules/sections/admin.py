from django.contrib import admin

from .models import Section, SectionCodeConfig, SectionStudent


# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'section_code', 'section_name')

class SectionStudentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'section', 'student')

class SectionCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Section, SectionAdmin)
admin.site.register(SectionStudent, SectionStudentAdmin)
admin.site.register(SectionCodeConfig, SectionCodeConfigAdmin)
