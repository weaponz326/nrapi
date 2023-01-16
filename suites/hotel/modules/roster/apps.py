from django.apps import AppConfig


class RosterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.roster'
    label = 'hotel_module_roster'
    verbose_name = 'hotel module roster'
