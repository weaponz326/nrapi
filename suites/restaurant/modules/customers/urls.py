from django.urls import path, include
from . import views


urlpatterns = [
    path('customer/', views.CustomerView.as_view()),
    path('customer/<id>', views.CustomerDetailView.as_view()),

    path('config/customer-code/<id>', views.CustomerCodeConfigDetailView.as_view()),
    path('config/new-customer-code/<id>', views.NewCustomerCodeConfigView.as_view()),
    path('dashboard/customer-count/', views.customer_count),
]