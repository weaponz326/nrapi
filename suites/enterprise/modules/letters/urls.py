from django.urls import path, include

from . import views


urlpatterns = [
    path('sent-letter/', views.SentLetterView.as_view()),
    path('sent-letter/<id>', views.SentLetterDetailView.as_view()),
    path('received-letter/', views.ReceivedLetterView.as_view()),
    path('received-letter/<id>', views.ReceivedLetterDetailView.as_view()),
]
