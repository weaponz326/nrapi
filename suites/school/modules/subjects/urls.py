from django.urls import path, include
from . import views


urlpatterns = [
    path('subject/', views.SubjectView.as_view()),
    path('subject/<id>', views.SubjectDetailView.as_view()),
    path('subject-teacher/', views.SubjectTeacherView.as_view()),
    path('subject-teacher/<id>', views.SubjectTeacherDetailView.as_view()),

    path('config/subject-code/<id>', views.SubjectCodeConfigDetailView.as_view()),
    path('config/new-subject-code/<id>', views.NewSubjectCodeConfigView.as_view()),
]