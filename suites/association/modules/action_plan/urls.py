from django.urls import path, include

from . import views


urlpatterns = [
    path('action-plan/', views.ActionPlanView.as_view()),
    path('action-plan/<id>', views.ActionPlanDetailView.as_view()),
    path('plan-step/', views.PlanStepView.as_view()),
    path('plan-step/<id>', views.PlanStepDetailView.as_view()),

    path('config/action-plan-code/<id>', views.ActionPlanCodeConfigDetailView.as_view()),
    path('config/new-action-plan-code/<id>', views.NewActionPlanCodeConfigView.as_view()),
]
