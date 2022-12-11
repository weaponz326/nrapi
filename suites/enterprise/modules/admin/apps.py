from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.admin'
    label = 'restaurant_module_admin'
    verbose_name = 'restaurant module admin'
