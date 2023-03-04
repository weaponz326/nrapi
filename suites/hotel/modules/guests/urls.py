from django.urls import path, include
from . import views


urlpatterns = [
    path('guest/', views.GuestView.as_view()),
    path('guest/<id>', views.GuestDetailView.as_view()),

    path('config/guest-code/<id>', views.GuestCodeConfigDetailView.as_view()),
    path('config/new-guest-code/<id>', views.NewGuestCodeConfigView.as_view()),
    path('dashboard/guest-count/', views.guest_count),
]