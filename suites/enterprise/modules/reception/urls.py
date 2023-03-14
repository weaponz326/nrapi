from django.urls import path, include

from . import views


urlpatterns = [
    path('visit/', views.VisitView.as_view()),
    path('visit/<id>', views.VisitDetailView.as_view()),

    path('config/visit-code/<id>', views.VisitCodeConfigDetailView.as_view()),
    path('config/new-visit-code/<id>', views.NewVisitCodeConfigView.as_view()),
]
