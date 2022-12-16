from django.urls import path, include

from . import views


urlpatterns = [
    path('appraisal/', views.AppraisalView.as_view()),
    path('appraisal/<id>', views.AppraisalDetailView.as_view()),
    path('appraisal-sheet/', views.AppraisalSheetView.as_view()),
    path('appraisal-sheet/<id>', views.AppraisalSheetDetailView.as_view()),
]
