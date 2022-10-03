from cProfile import label
from django.apps import AppConfig


class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.personal.modules.notes'
    label = 'personal_module_notes'
    verbose_name = 'personal module notes'
