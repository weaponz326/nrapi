from django.urls import path, include
from . import views


urlpatterns = [
    path('timetable/', views.TimetableView.as_view()),
    path('timetable/<id>', views.TimetableDetailView.as_view()),
    path('timetable-class/', views.TimetableClassView.as_view()),
    path('timetable-class/<id>', views.TimetableClassDetailView.as_view()),
    path('timetable-period/', views.TimetablePeriodView.as_view()),
    path('timetable-period/<id>', views.TimetablePeriodDetailView.as_view()),

    path('config/timetable-code/<id>', views.TimetableCodeConfigDetailView.as_view()),
    path('config/new-timetable-code/<id>', views.NewTimetableCodeConfigView.as_view()),
]