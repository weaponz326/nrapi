from django.urls import path, include
from . import views


urlpatterns = [
    path('group/', views.GroupView.as_view()),
    path('group/<id>', views.GroupDetailView.as_view()),
    path('group-member/', views.GroupMemberView.as_view()),
    path('group-member/<id>', views.GroupMemberDetailView.as_view()),

    path('config/group-code/<id>', views.GroupCodeConfigDetailView.as_view()),
    path('config/new-group-code/<id>', views.NewGroupCodeConfigView.as_view()),
]