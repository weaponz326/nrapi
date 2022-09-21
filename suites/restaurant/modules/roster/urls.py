from django.urls import path, include

from . import views


urlpatterns = [
    path('roster/', views.RosterView.as_view()),
    path('roster/<id>', views.RosterDetailView.as_view()),
    path('shift/', views.ShiftView.as_view()),
    path('shift/<id>', views.ShiftDetailView.as_view()),
    path('batch/', views.BatchView.as_view()),
    path('batch/<id>', views.BatchDetailView.as_view()),
    path('personnel/', views.StaffPersonnelView.as_view()),
    path('personnel/<id>', views.StaffPersonnelDetailView.as_view()),
    path('roster-day/', views.RosterDayView.as_view()),
    path('roster-day/<id>', views.RosterDayDetailView.as_view()),

    path('dashboard/roster-count', views.roster_count),
]
