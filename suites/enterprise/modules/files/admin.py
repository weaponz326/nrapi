from django.contrib import admin

from .models import File, Folder


# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'folder_number', 'folder_name')

class FileAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'file_number', 'file_name', 'file_type', 'date_added')

admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
