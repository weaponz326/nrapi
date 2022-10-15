from django.urls import path, include

from . import views


urlpatterns = [
    path('student/', views.StudentView.as_view()),
    path('student/<id>', views.StudentDetailView.as_view()),

    path('config/student-code/<id>', views.StudentCodeConfigDetailView.as_view()),
    path('config/new-student-code/<id>', views.NewStudentCodeConfigView.as_view()),
]