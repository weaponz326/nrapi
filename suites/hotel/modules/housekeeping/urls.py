from django.urls import path, include

from . import views


urlpatterns = [
    path('housekeeping/', views.HousekeepingView.as_view()),
    path('housekeeping/<id>', views.HousekeepingDetailView.as_view()),
    path('checklist/', views.ChecklistView.as_view()),
    path('checklist/<id>', views.ChecklistDetailView.as_view()),

    path('config/housekeeping-code/<id>', views.HousekeepingCodeConfigDetailView.as_view()),
    path('config/new-housekeeping-code/<id>', views.NewHousekeepingCodeConfigView.as_view()),
    path('dashboard/housekeeping-count/', views.housekeeping_count),
    path('dashboard/housekeeping-annotate/', views.housekeeping_annotate),
]
