from django.urls import path, include

from . import views


urlpatterns = [
    path('leave/', views.LeaveView.as_view()),
    path('leave/<id>', views.LeaveDetailView.as_view()),
]
