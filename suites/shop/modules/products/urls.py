from django.urls import path, include

from . import views


urlpatterns = [
    path('product/', views.ProductView.as_view()),
    path('product/<id>', views.ProductDetailView.as_view()),

    path('config/product-code/<id>', views.ProductCodeConfigDetailView.as_view()),
    path('config/new-product-code/<id>', views.NewProductCodeConfigView.as_view()),
]