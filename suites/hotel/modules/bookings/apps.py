from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.bookings'
    label = 'hotel_module_bookings'
    verbose_name = 'hotel module bookings'
