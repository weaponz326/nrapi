from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink/<id>', views.RinkDetailView.as_view()),
    path('rink-list/', views.AllRinkView.as_view()),

    path('dashboard/rink-share-count/', views.rink_share_count),
    path('dashboard/rink-share-annotate/', views.rink_share_annotate),
]
