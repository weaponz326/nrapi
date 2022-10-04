from django.urls import path, include

from . import views


urlpatterns = [
    path('staff/', views.StaffView.as_view()),
    path('staff/<id>', views.StaffDetailView.as_view()),

    path('config/staff-code/<id>', views.StaffCodeConfigDetailView.as_view()),
    path('config/new-staff-code/<id>', views.NewStaffCodeConfigView.as_view()),
    path('dashboard/staff-count', views.staff_count),
]