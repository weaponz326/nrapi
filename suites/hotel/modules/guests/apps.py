from django.apps import AppConfig


class GuestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.guests'
    label = 'hotel_module_guests'
    verbose_name = 'hotel module guests'
