from django.urls import path, include
from . import views


urlpatterns = [
    path('supplier/', views.SupplierView.as_view()),
    path('supplier/<id>', views.SupplierDetailView.as_view()),
    path('supplier-item/', views.SupplierItemView.as_view()),
    path('supplier-item/<id>', views.SupplierItemDetailView.as_view()),

    path('config/supplier-code/<id>', views.SupplierCodeConfigDetailView.as_view()),
    path('config/new-supplier-code/<id>', views.NewSupplierCodeConfigView.as_view()),
    path('dashboard/supplier-count/', views.supplier_count),
]