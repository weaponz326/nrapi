from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.staff'
    label = 'hospital_module_staff'
    verbose_name = 'hospital module staff'
