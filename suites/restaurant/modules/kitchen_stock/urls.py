from django.urls import path, include

from . import views


urlpatterns = [
    path('stock-item/', views.StockItemView.as_view()),
    path('stock-item/<id>', views.StockItemDetailView.as_view()),

    path('dashboard/stock-item-count/', views.stock_item_count),
    path('dashboard/out-of-stock-count/', views.out_of_stock_count),
]