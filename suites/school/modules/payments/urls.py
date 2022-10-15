from django.urls import path, include
from . import views


urlpatterns = [
    path('payment/', views.PaymentView.as_view()),
    path('payment/<id>', views.PaymentDetailView.as_view()),

    path('config/payment-code/<id>', views.PaymentCodeConfigDetailView.as_view()),
    path('config/new-payment-code/<id>', views.NewPaymentCodeConfigView.as_view()),
]