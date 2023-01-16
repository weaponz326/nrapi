from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.settings'
    label = 'hotel_module_settings'
    verbose_name = 'hotel module settings'
