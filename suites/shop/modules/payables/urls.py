from django.urls import path, include

from . import views


urlpatterns = [
    path('payable/', views.PayableView.as_view()),
    path('payable/<id>', views.PayableDetailView.as_view()),

    path('config/payable-code/<id>', views.PayableCodeConfigDetailView.as_view()),
    path('config/new-payable-code/<id>', views.NewPayableCodeConfigView.as_view()),
    path('dashboard/payable-count/', views.payable_count),
]