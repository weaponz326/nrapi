from django.urls import path, include

from . import views


urlpatterns = [
    path('booking/', views.BookingView.as_view()),
    path('booking/<id>', views.BookingDetailView.as_view()),
    path('booked-room/', views.BookedRoomView.as_view()),
    path('booked-room/<id>', views.BookedRoomDetailView.as_view()),

    path('config/booking-code/<id>', views.BookingCodeConfigDetailView.as_view()),
    path('config/new-booking-code/<id>', views.NewBookingCodeConfigView.as_view()),
    path('dashboard/booking-count/', views.booking_count),
    path('dashboard/booking-annotate/', views.booking_annotate),
]
