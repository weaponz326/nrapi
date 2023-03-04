from django.urls import path, include
from . import views


urlpatterns = [
    path('ward/', views.WardView.as_view()),
    path('ward/<id>', views.WardDetailView.as_view()),
    path('ward-patient/', views.WardPatientView.as_view()),
    path('ward-patient/<id>', views.WardPatientDetailView.as_view()),

    path('config/ward-code/<id>', views.WardCodeConfigDetailView.as_view()),
    path('config/new-ward-code/<id>', views.NewWardCodeConfigView.as_view()),
]