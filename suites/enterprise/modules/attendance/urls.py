from django.urls import path, include
from . import views


urlpatterns = [
    path('attendance/', views.AttendanceView.as_view()),
    path('attendance/<id>', views.AttendanceDetailView.as_view()),

    path('config/attendance-code/<id>', views.AttendanceCodeConfigDetailView.as_view()),
    path('config/new-attendance-code/<id>', views.NewAttendanceCodeConfigView.as_view()),
]