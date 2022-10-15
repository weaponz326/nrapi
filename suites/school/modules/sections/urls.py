from django.urls import path, include
from . import views


urlpatterns = [
    path('section/', views.SectionView.as_view()),
    path('section/<id>', views.SectionDetailView.as_view()),
    path('section-student/', views.SectionStudentView.as_view()),
    path('section-student/<id>', views.SectionStudentDetailView.as_view()),

    path('config/section-code/<id>', views.SectionCodeConfigDetailView.as_view()),
    path('config/new-section-code/<id>', views.NewSectionCodeConfigView.as_view()),
]