from django.urls import path, include

from . import views


urlpatterns = [
    path('visitor/', views.VisitorView.as_view()),
    path('visitor/<id>', views.VisitorDetailView.as_view()),
]
