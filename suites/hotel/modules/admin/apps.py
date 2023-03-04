from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.admin'
    label = 'hotel_module_admin'
    verbose_name = 'hotel module admin'
