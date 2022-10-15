from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.school.modules.settings'
    label = 'school_module_settings'
    verbose_name = 'school module settings'
