from django.urls import path, include
from . import views


urlpatterns = [
    path('customer/', views.CustomerView.as_view()),
    path('customer/<id>', views.CustomerDetailView.as_view()),

    path('dashboard/customer-count/', views.customer_count),
]