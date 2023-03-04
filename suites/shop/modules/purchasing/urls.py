from django.urls import path, include

from . import views


urlpatterns = [
    path('purchasing/', views.PurchasingView.as_view()),
    path('purchasing/<id>', views.PurchasingDetailView.as_view()),
    path('purchasing-item/', views.PurchasingItemView.as_view()),
    path('purchasing-item/<id>', views.PurchasingItemDetailView.as_view()),

    path('config/purchasing-code/<id>', views.PurchasingCodeConfigDetailView.as_view()),
    path('config/new-purchasing-code/<id>', views.NewPurchasingCodeConfigView.as_view()),
    path('dashboard/purchasing-count/', views.purchasing_count),
    path('dashboard/purchasing-annotate/', views.purchasing_annotate),
]
