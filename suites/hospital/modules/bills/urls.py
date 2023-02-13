from django.urls import path, include

from . import views


urlpatterns = [
    path('bill/', views.BillView.as_view()),
    path('bill/<id>', views.BillDetailView.as_view()),

    path('config/bill-code/<id>', views.BillCodeConfigDetailView.as_view()),
    path('config/new-bill-code/<id>', views.NewBillCodeConfigView.as_view()),
]