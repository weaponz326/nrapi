from django.urls import path, include

from . import views


urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointment/<id>', views.AppointmentDetailView.as_view()),

    path('config/appointment-code/<id>', views.AppointmentCodeConfigDetailView.as_view()),
    path('config/new-appointment-code/<id>', views.NewAppointmentCodeConfigView.as_view()),
]