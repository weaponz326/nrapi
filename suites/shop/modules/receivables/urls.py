from django.urls import path, include

from . import views


urlpatterns = [
    path('receivable/', views.ReceivableView.as_view()),
    path('receivable/<id>', views.ReceivableDetailView.as_view()),

    path('config/receivable-code/<id>', views.ReceivableCodeConfigDetailView.as_view()),
    path('config/new-receivable-code/<id>', views.NewReceivableCodeConfigView.as_view()),
    path('dashboard/receivable-count/', views.receivable_count),
]