from django.urls import path, include

from . import views


urlpatterns = [
    path('dispense/', views.DispenseView.as_view()),
    path('dispense/<id>', views.DispenseDetailView.as_view()),
    path('dispense-item/', views.DispenseItemView.as_view()),
    path('dispense-item/<id>', views.DispenseItemDetailView.as_view()),

    path('config/dispense-code/<id>', views.DispenseCodeConfigDetailView.as_view()),
    path('config/new-dispense-code/<id>', views.NewDispenseCodeConfigView.as_view()),
]