from django.urls import path, include

from . import views


urlpatterns = [
    path('admission/', views.AdmissionView.as_view()),
    path('admission/<id>', views.AdmissionDetailView.as_view()),

    path('config/admission-code/<id>', views.AdmissionCodeConfigDetailView.as_view()),
    path('config/new-admission-code/<id>', views.NewAdmissionCodeConfigView.as_view()),
]