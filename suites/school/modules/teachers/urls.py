from django.urls import path, include

from . import views


urlpatterns = [
    path('teacher/', views.TeacherView.as_view()),
    path('teacher/<id>', views.TeacherDetailView.as_view()),

    path('config/teacher-code/<id>', views.TeacherCodeConfigDetailView.as_view()),
    path('config/new-teacher-code/<id>', views.NewTeacherCodeConfigView.as_view()),
]