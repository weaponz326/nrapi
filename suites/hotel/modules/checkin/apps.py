from django.apps import AppConfig


class CheckinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.checkin'
    label = 'hotel_module_checkin'
    verbose_name = 'hotel module checkin'
