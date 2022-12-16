from django.urls import path, include

from . import views


urlpatterns = [
    path('procurement/', views.ProcurementView.as_view()),
    path('procurement/<id>', views.ProcurementDetailView.as_view()),
    path('order-review/', views.OrderReviewView.as_view()),
    path('order-review/<id>', views.OrderReviewDetailView.as_view()),
]
