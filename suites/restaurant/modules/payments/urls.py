from django.urls import path, include

from . import views


urlpatterns = [
    path('payment/', views.PaymentView.as_view()),
    path('payment/<id>', views.PaymentDetailView.as_view()),

    path('dashboard/payment-count', views.payment_count),
    path('dashboard/payment-total', views.payment_total),
    path('dashboard/payment-annotate', views.payment_annotate),
]