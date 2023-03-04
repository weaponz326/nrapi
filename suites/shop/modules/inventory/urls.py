from django.urls import path, include

from . import views


urlpatterns = [
    path('inventory/', views.InventoryView.as_view()),
    path('inventory/<id>', views.InventoryDetailView.as_view()),

    path('config/inventory-code/<id>', views.InventoryCodeConfigDetailView.as_view()),
    path('config/new-inventory-code/<id>', views.NewInventoryCodeConfigView.as_view()),
    path('dashboard/inventory-count/', views.inventory_count),
    path('dashboard/out-of-stock-count/', views.out_of_stock_count),
]