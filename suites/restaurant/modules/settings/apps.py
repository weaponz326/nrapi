from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.settings'
    label = 'restaurant_settings'
    verbose_name = 'restaurant module settings'
