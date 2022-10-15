from django.urls import path, include
from . import views


urlpatterns = [
    path('lesson-plan/', views.LessonPlanView.as_view()),
    path('lesson-plan/<id>', views.LessonPlanDetailView.as_view()),

    path('config/lesson-plan-code/<id>', views.LessonPlanCodeConfigDetailView.as_view()),
    path('config/new-lesson-plan-code/<id>', views.NewLessonPlanCodeConfigView.as_view()),
]