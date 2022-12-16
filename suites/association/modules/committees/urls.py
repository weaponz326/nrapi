from django.urls import path, include
from . import views


urlpatterns = [
    path('committee/', views.CommitteeView.as_view()),
    path('committee/<id>', views.CommitteeDetailView.as_view()),
    path('committee-member/', views.CommitteeMemberView.as_view()),
    path('committee-member/<id>', views.CommitteeMemberDetailView.as_view()),
]