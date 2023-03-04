from django.apps import AppConfig


class RosterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.roster'
    label = 'restaurant_module_roster'
    verbose_name = 'restaurant module roster'
