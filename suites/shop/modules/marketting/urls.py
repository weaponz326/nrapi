from django.urls import path, include

from . import views


urlpatterns = [
    path('campaign/', views.CampaignView.as_view()),
    path('campaign/<id>', views.CampaignDetailView.as_view()),

    path('config/campaign-code/<id>', views.CampaignCodeConfigDetailView.as_view()),
    path('config/new-campaign-code/<id>', views.NewCampaignCodeConfigView.as_view()),
    path('dashboard/campaign-count/', views.campaign_count),
]