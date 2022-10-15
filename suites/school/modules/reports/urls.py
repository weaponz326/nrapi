from django.urls import path, include
from . import views


urlpatterns = [
    path('report/', views.ReportView.as_view()),
    path('report/<id>', views.ReportDetailView.as_view()),
    path('report-assessment/', views.ReportAssessmentView.as_view()),
    path('report-assessment/<id>', views.ReportAssessmentDetailView.as_view()),

    path('config/report-code/<id>', views.ReportCodeConfigDetailView.as_view()),
    path('config/new-report-code/<id>', views.NewReportCodeConfigView.as_view()),
]