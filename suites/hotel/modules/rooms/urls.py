from django.urls import path, include
from . import views


urlpatterns = [
    path('room/', views.RoomView.as_view()),
    path('room/<id>', views.RoomDetailView.as_view()),

    path('dashboard/room-count/', views.room_count),
]