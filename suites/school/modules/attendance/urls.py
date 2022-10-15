from django.urls import path, include
from . import views


urlpatterns = [
    path('student-attendance/', views.StudentAttendanceView.as_view()),
    path('student-attendance/<id>', views.StudentAttendanceDetailView.as_view()),
    path('teacher-attendance/', views.TeacherAttendanceView.as_view()),
    path('teacher-attendance/<id>', views.TeacherAttendanceDetailView.as_view()),

    path('config/attendance-code/<id>', views.AttendanceCodeConfigDetailView.as_view()),
    path('config/new-attendance-code/<id>', views.NewAttendanceCodeConfigView.as_view()),
]