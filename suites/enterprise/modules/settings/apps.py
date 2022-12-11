from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.settings'
    label = 'enterprise_module_settings'
    verbose_name = 'enterprise module settings'
