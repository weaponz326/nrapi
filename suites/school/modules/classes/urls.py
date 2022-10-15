from django.urls import path, include
from . import views


urlpatterns = [
    path('class/', views.ClassView.as_view()),
    path('class/<id>', views.ClassDetailView.as_view()),
    path('class-student/', views.ClassStudentView.as_view()),
    path('class-student/<id>', views.ClassStudentDetailView.as_view()),
    path('department/', views.DepartmentView.as_view()),
    path('department/<id>', views.DepartmentDetailView.as_view()),
]