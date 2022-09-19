from django.urls import path, include

from . import views


urlpatterns = [
    path('calendar/', views.CalendarView.as_view()),
    path('calendar/<id>', views.CalendarDetailView.as_view()),
    path('schedule/', views.ScheduleView.as_view()),
    path('schedule/<id>', views.ScheduleDetailView.as_view()),
    path('all-schedule/', views.AllScheduleView.as_view()),

    path('dashboard/calendar-count/', views.calendar_count),
    path('dashboard/schedule-count/', views.schedule_count),
    path('dashboard/calendar-annotate/', views.calendar_annotate),
    path('dashboard/schedule-annotate/', views.schedule_annotate),
]
