from django.urls import path, include

from . import views


urlpatterns = [
    path('asset/', views.AssetView.as_view()),
    path('asset/<id>', views.AssetDetailView.as_view()),

    path('config/asset-code/<id>', views.AssetCodeConfigDetailView.as_view()),
    path('config/new-asset-code/<id>', views.NewAssetCodeConfigView.as_view()),
]
