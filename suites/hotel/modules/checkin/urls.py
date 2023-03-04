from django.urls import path, include

from . import views


urlpatterns = [
    path('checkin/', views.CheckinView.as_view()),
    path('checkin/<id>', views.CheckinDetailView.as_view()),

    path('config/checkin-code/<id>', views.CheckinCodeConfigDetailView.as_view()),
    path('config/new-checkin-code/<id>', views.NewCheckinCodeConfigView.as_view()),
    path('dashboard/checkin-count/', views.checkin_count),
    path('dashboard/checkin-annotate/', views.checkin_annotate),
]
