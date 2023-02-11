from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.settings'
    label = 'hospital_module_settings'
    verbose_name = 'hospital module settings'
