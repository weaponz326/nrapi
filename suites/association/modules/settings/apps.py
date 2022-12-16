from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.association.modules.settings'
    label = 'association_module_settings'
    verbose_name = 'association module settings'
