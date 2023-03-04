from django.urls import path, include

from . import views


urlpatterns = [
    path('invoice/', views.InvoiceView.as_view()),
    path('invoice/<id>', views.InvoiceDetailView.as_view()),
    path('invoice-item/', views.InvoiceItemView.as_view()),
    path('invoice-item/<id>', views.InvoiceItemDetailView.as_view()),

    path('config/invoice-code/<id>', views.InvoiceCodeConfigDetailView.as_view()),
    path('config/new-invoice-code/<id>', views.NewInvoiceCodeConfigView.as_view()),
    path('dashboard/invoice-count/', views.invoice_count),
    path('dashboard/invoice-annotate/', views.invoice_annotate),
]
