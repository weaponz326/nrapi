from django.urls import path, include

from . import views


urlpatterns = [
    path('bill/', views.BillView.as_view()),
    path('bill/<id>', views.BillDetailView.as_view()),
    path('checkin-charge/', views.CheckinChargeView.as_view()),
    path('checkin-charge/<id>', views.CheckinChargeDetailView.as_view()),
    path('service-charge/', views.ServiceChargeView.as_view()),
    path('service-charge/<id>', views.ServiceChargeDetailView.as_view()),

    path('config/bill-code/<id>', views.BillCodeConfigDetailView.as_view()),
    path('config/new-bill-code/<id>', views.NewBillCodeConfigView.as_view()),
    path('dashboard/bill-count/', views.bill_count),
    path('dashboard/bill-annotate/', views.bill_annotate),
]
