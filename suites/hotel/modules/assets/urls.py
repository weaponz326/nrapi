from django.urls import path, include

from . import views


urlpatterns = [
    path('asset/', views.AssetView.as_view()),
    path('asset/<id>', views.AssetDetailView.as_view()),
]
