from django.urls import path, include
from . import views


urlpatterns = [
    path('fees/', views.FeesView.as_view()),
    path('fees/<id>', views.FeesDetailView.as_view()),
    path('fees-target/', views.FeesTargetView.as_view()),
    path('fees-target/<id>', views.FeesTargetDetailView.as_view()),

    path('config/fees-code/<id>', views.FeesCodeConfigDetailView.as_view()),
    path('config/new-fees-code/<id>', views.NewFeesCodeConfigView.as_view()),
]