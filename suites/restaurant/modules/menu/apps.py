from django.apps import AppConfig


class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.menu'
    label = 'restaurant_module_menu'
    verbose_name = 'restaurant module menu'
