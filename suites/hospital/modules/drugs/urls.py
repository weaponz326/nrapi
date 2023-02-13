from django.urls import path, include

from . import views


urlpatterns = [
    path('drug/', views.DrugView.as_view()),
    path('drug/<id>', views.DrugDetailView.as_view()),

    path('config/drug-code/<id>', views.DrugCodeConfigDetailView.as_view()),
    path('config/new-drug-code/<id>', views.NewDrugCodeConfigView.as_view()),
]