from django.urls import path, include

from . import views


urlpatterns = [
    path('folder/', views.FolderView.as_view()),
    path('folder/<id>', views.FolderDetailView.as_view()),
    path('file/', views.FileView.as_view()),
    path('file/<id>', views.FileDetailView.as_view()),
]
