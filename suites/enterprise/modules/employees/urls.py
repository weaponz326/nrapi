from django.urls import path, include

from . import views


urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
    path('employee/<id>', views.EmployeeDetailView.as_view()),

    path('config/employee-code/<id>', views.EmployeeCodeConfigDetailView.as_view()),
    path('config/new-employee-code/<id>', views.NewEmployeeCodeConfigView.as_view()),
]