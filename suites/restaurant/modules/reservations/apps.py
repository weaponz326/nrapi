from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.reservations'
    label = 'restaurant_module_reservations'
    verbose_name = 'restaurant module reservations'
