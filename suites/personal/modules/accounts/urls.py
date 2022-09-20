from django.urls import path, include

from . import views


urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<id>', views.AccountDetailView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('transaction/<id>', views.TransactionDetailView.as_view()),
    path('all-transaction/', views.AllTransactionsView.as_view()),

    path('dashboard/all-account-count/', views.all_account_count),
    path('dashboard/transaction-share/', views.transaction_share),
    path('dashboard/transaction-annotate/', views.transaction_annotate),
]
