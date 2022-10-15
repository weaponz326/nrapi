from django.urls import path, include
from . import views


urlpatterns = [
    path('parent/', views.ParentView.as_view()),
    path('parent/<id>', views.ParentDetailView.as_view()),
    path('parent-ward/', views.ParentWardView.as_view()),
    path('parent-ward/<id>', views.ParentWardDetailView.as_view()),

    path('config/parent-code/<id>', views.ParentCodeConfigDetailView.as_view()),
    path('config/new-parent-code/<id>', views.NewParentCodeConfigView.as_view()),
]