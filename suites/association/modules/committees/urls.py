from django.urls import path, include
from . import views


urlpatterns = [
    path('committee/', views.CommitteeView.as_view()),
    path('committee/<id>', views.CommitteeDetailView.as_view()),
    path('committee-member/', views.CommitteeMemberView.as_view()),
    path('committee-member/<id>', views.CommitteeMemberDetailView.as_view()),

    path('config/committee-code/<id>', views.CommitteeCodeConfigDetailView.as_view()),
    path('config/new-committee-code/<id>', views.NewCommitteeCodeConfigView.as_view()),
]