from django.urls import path, include
from . import views


urlpatterns = [
    path('support/', views.SupportView.as_view()),
]
