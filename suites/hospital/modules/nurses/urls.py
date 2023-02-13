from django.urls import path, include

from . import views


urlpatterns = [
    path('nurse/', views.NurseView.as_view()),
    path('nurse/<id>', views.NurseDetailView.as_view()),

    path('config/nurse-code/<id>', views.NurseCodeConfigDetailView.as_view()),
    path('config/new-nurse-code/<id>', views.NewNurseCodeConfigView.as_view()),
]