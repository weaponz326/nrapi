from django.urls import path, include
from . import views


urlpatterns = [
    path('term/', views.TermView.as_view()),
    path('term/<id>', views.TermDetailView.as_view()),
    path('active-term/<id>', views.ActiveTermDetailView.as_view()),

    path('config/term-code/<id>', views.TermCodeConfigDetailView.as_view()),
    path('config/new-term-code/<id>', views.NewTermCodeConfigView.as_view()),
]