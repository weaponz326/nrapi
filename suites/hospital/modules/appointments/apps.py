from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.appointments'
    label = 'hospital_module_appointments'
    verbose_name = 'hospital module appointments'
