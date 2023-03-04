from django.urls import path, include

from . import views


urlpatterns = [
    path('sales/', views.SalesView.as_view()),
    path('sales/<id>', views.SalesDetailView.as_view()),

    path('config/sales-code/<id>', views.SalesCodeConfigDetailView.as_view()),
    path('config/new-sales-code/<id>', views.NewSalesCodeConfigView.as_view()),
    path('dashboard/sales-count/', views.sales_count),
]