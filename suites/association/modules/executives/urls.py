from django.urls import path, include
from . import views


urlpatterns = [
    path('executive/', views.ExecutiveView.as_view()),
    path('executive/<id>', views.ExecutiveDetailView.as_view()),
]