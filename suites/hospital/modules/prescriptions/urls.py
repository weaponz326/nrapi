from django.urls import path, include

from . import views


urlpatterns = [
    path('prescription/', views.PrescriptionView.as_view()),
    path('prescription/<id>', views.PrescriptionDetailView.as_view()),
    path('prescription-item/', views.PrescriptionItemView.as_view()),
    path('prescription-item/<id>', views.PrescriptionItemDetailView.as_view()),

    path('config/prescription-code/<id>', views.PrescriptionCodeConfigDetailView.as_view()),
    path('config/new-prescription-code/<id>', views.NewPrescriptionCodeConfigView.as_view()),
]