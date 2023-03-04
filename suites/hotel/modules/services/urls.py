from django.urls import path, include

from . import views


urlpatterns = [
    path('service/', views.ServiceView.as_view()),
    path('service/<id>', views.ServiceDetailView.as_view()),
    path('service-item/', views.ServiceItemView.as_view()),
    path('service-item/<id>', views.ServiceItemDetailView.as_view()),

    path('config/service-code/<id>', views.ServiceCodeConfigDetailView.as_view()),
    path('config/new-service-code/<id>', views.NewServiceCodeConfigView.as_view()),
    path('dashboard/service-count/', views.service_count),
    path('dashboard/service-annotate/', views.service_annotate),
]
