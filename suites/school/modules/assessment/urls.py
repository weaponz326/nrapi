from django.urls import path, include
from . import views


urlpatterns = [
    path('assessment/', views.AssessmentView.as_view()),
    path('assessment/<id>', views.AssessmentDetailView.as_view()),
    path('assessment-sheet/', views.AssessmentSheetView.as_view()),
    path('assessment-sheet/<id>', views.AssessmentSheetDetailView.as_view()),

    path('config/assessment-code/<id>', views.AssessmentCodeConfigDetailView.as_view()),
    path('config/new-assessment-code/<id>', views.NewAssessmentCodeConfigView.as_view()),
]