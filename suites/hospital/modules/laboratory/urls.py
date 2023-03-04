from django.urls import path, include

from . import views


urlpatterns = [
    path('lab/', views.LaboratoryView.as_view()),
    path('lab/<id>', views.LaboratoryDetailView.as_view()),

    path('config/lab-code/<id>', views.LaboratoryCodeConfigDetailView.as_view()),
    path('config/new-lab-code/<id>', views.NewLaboratoryCodeConfigView.as_view()),
]