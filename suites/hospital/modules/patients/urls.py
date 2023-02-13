from django.urls import path, include

from . import views


urlpatterns = [
    path('patient/', views.PatientView.as_view()),
    path('patient/<id>', views.PatientDetailView.as_view()),

    path('config/patient-code/<id>', views.PatientCodeConfigDetailView.as_view()),
    path('config/new-patient-code/<id>', views.NewPatientCodeConfigView.as_view()),
]