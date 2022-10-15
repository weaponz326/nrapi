from django.contrib import admin

from .models import ActiveTerm, Term, TermCodeConfig


# Register your models here.

class TermAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'term_code', 'term_name', 'academic_year', 'term_status')

class ActiveTermAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'term')

class TermCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Term, TermAdmin)
admin.site.register(ActiveTerm, ActiveTermAdmin)
admin.site.register(TermCodeConfig, TermCodeConfigAdmin)
