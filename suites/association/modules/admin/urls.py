from django.urls import path, include
from . import views

urlpatterns = [
    path('account-user/', views.AccountUserView.as_view()),
    path('account-user/<id>', views.AccountUserDetailView.as_view()),
    path('account-user-account/', views.AccountUserAccountView.as_view()),
    path('access/', views.AccessView.as_view()),
    path('access/<id>', views.AccessDetailView.as_view()),
    path('invitation/', views.InvitationView.as_view()),
    path('invitation/<id>', views.InvitationDetailView.as_view()),

    path('dashboard/account-user-count', views.account_user_count),
]
