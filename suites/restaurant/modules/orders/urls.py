from django.urls import path, include

from . import views


urlpatterns = [
    path('order/', views.OrderView.as_view()),
    path('order/<id>', views.OrderDetailView.as_view()),
    path('order-item/', views.OrderItemView.as_view()),
    path('order-item/<id>', views.OrderItemDetailView.as_view()),

    path('dashboard/order-count/', views.order_count),
    path('dashboard/order-annotate/', views.order_annotate),
]
