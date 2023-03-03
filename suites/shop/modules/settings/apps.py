from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.settings'
    label = 'shop_module_settings'
    verbose_name = 'shop module settings'
