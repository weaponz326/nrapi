from django.urls import path, include

from . import views


urlpatterns = [
    path('extended-profile/', views.ExtendedProfileView.as_view()),
    path('extended-profile/<id>', views.ExtendedProfileDetailView.as_view()),
    path('invitation/', views.InvitationView.as_view()),
    path('invitation/<id>', views.InvitationDetailView.as_view()),
    path('all-user-suite-account/', views.AllUserSuiteAccountView.as_view()),
    path('user-suite-account/<id>', views.AllUserSuiteAccountDetailView.as_view()),

    path('dashboard/all-user-suite-account-count/', views.all_user_suite_account_count),
    path('dashboard/user-suite-account-share/', views.user_suite_account_share),
]
