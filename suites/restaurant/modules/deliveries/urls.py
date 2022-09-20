from django.urls import path, include
from . import views


urlpatterns = [
    path('delivery/', views.DeliveryView.as_view()),
    path('delivery/<id>', views.DeliveryDetailView.as_view()),

    path('dashboard/delivery-count/', views.delivery_count),
    path('dashboard/delivery-annotate/', views.delivery_annotate),
]