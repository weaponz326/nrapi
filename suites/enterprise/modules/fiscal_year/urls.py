from django.urls import path, include
from . import views


urlpatterns = [
    path('fiscal-year/', views.FiscalYearView.as_view()),
    path('fiscal-year/<id>', views.FiscalYearDetailView.as_view()),
    path('active-fiscal-year/<id>', views.ActiveFiscalYearDetailView.as_view()),

    path('config/fiscal-year-code/<id>', views.FiscalYearCodeConfigDetailView.as_view()),
    path('config/new-fiscal-year-code/<id>', views.NewFiscalYearCodeConfigView.as_view()),
]