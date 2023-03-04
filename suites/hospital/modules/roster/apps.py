from django.apps import AppConfig


class RosterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.roster'
    label = 'hospital_module_roster'
    verbose_name = 'hospital module roster'
