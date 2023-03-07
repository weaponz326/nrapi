from django.urls import path, include
from . import views


urlpatterns = [
    path('task-group/', views.TaskGroupView.as_view()),
    path('task-group/<id>', views.TaskGroupDetailView.as_view()),
    path('all-task-item/', views.AllTaskItemView.as_view()),
    path('task-item/', views.TaskItemView.as_view()),
    path('task-item/<id>', views.TaskItemDetailView.as_view()),

    path('config/task-group-code/<id>', views.TaskGroupCodeConfigDetailView.as_view()),
    path('config/new-task-group-code/<id>', views.NewTaskGroupCodeConfigView.as_view()),
    path('config/task-item-code/<id>', views.TaskItemCodeConfigDetailView.as_view()),
    path('config/new-task-item-code/<id>', views.NewTaskItemCodeConfigView.as_view()),

    path('dashboard/task-group-count/', views.task_group_count),
    path('dashboard/task-item-count/', views.task_item_count),
    path('dashboard/all-todo-count/', views.all_todo_count),
    path('dashboard/task-group-annotate/', views.task_group_annotate),
    path('dashboard/task-item-annotate/', views.task_item_annotate),
]
