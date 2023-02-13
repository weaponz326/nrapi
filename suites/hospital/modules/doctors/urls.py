from django.urls import path, include

from . import views


urlpatterns = [
    path('doctor/', views.DoctorView.as_view()),
    path('doctor/<id>', views.DoctorDetailView.as_view()),

    path('config/doctor-code/<id>', views.DoctorCodeConfigDetailView.as_view()),
    path('config/new-doctor-code/<id>', views.NewDoctorCodeConfigView.as_view()),
]