from django.urls import path, include

from . import views


urlpatterns = [
    path('note/', views.NoteView.as_view()),
    path('note/<id>', views.NoteDetailView.as_view()),
    path('note-search/', views.NoteSearchView.as_view()),

    path('dashboard/note-count/', views.note_count),
    path('dashboard/note-annotate/', views.note_annotate),
]
