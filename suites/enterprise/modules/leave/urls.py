from django.urls import path, include

from . import views


urlpatterns = [
    path('leave/', views.LeaveView.as_view()),
    path('leave/<id>', views.LeaveDetailView.as_view()),

    path('config/leave-code/<id>', views.LeaveCodeConfigDetailView.as_view()),
    path('config/new-leave-code/<id>', views.NewLeaveCodeConfigView.as_view()),
]
