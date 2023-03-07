from django.contrib import admin

from .models import Note, NoteCodeConfig


# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'title', 'created_at')

class NoteCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Note, NoteAdmin)
admin.site.register(NoteCodeConfig, NoteCodeConfigAdmin)
