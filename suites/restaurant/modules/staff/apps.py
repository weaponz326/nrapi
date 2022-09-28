from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.staff'
    label = 'restaurant_module_staff'
    verbose_name = 'restaurant module staff'
