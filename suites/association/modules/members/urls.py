from django.urls import path, include

from . import views


urlpatterns = [
    path('member/', views.MemberView.as_view()),
    path('member/<id>', views.MemberDetailView.as_view()),

    # path('config/member-code/<id>', views.MemberCodeConfigDetailView.as_view()),
    # path('config/new-member-code/<id>', views.NewMemberCodeConfigView.as_view()),
]