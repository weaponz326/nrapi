from django.urls import path, include

from . import views


urlpatterns = [
    path('search-list/', views.UserSearchView.as_view()),
    path('search-detail/<id>', views.UserDetailView.as_view()),
]
