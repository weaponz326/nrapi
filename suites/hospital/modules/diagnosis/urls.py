from django.urls import path, include

from . import views


urlpatterns = [
    path('diagnosis/', views.DiagnosisView.as_view()),
    path('diagnosis/<id>', views.DiagnosisDetailView.as_view()),
    path('diagnosis-report/<id>', views.DiagnosisReportDetailView.as_view()),

    path('config/diagnosis-code/<id>', views.DiagnosisCodeConfigDetailView.as_view()),
    path('config/new-diagnosis-code/<id>', views.NewDiagnosisCodeConfigView.as_view()),
]