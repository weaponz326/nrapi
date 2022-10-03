from cProfile import label
from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.personal.modules.settings'
    label = 'personal_module_settings'
    verbose_name = 'personal module settings'
