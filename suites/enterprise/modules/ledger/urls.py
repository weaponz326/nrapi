from django.urls import path, include

from . import views


urlpatterns = [
    path('ledger/', views.LedgerView.as_view()),
    path('ledger/<id>', views.LedgerDetailView.as_view()),
    path('ledger-item/', views.LedgerItemView.as_view()),
    path('ledger-item/<id>', views.LedgerItemDetailView.as_view()),

    path('config/ledger-code/<id>', views.LedgerCodeConfigDetailView.as_view()),
    path('config/new-ledger-code/<id>', views.NewLedgerCodeConfigView.as_view()),

    path('dashboard/all-ledger-count/', views.all_ledger_count),
    path('dashboard/ledger-share/', views.item_share),
    path('dashboard/ledger-annotate/', views.item_annotate),
]
