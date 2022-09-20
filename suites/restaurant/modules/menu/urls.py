from django.urls import path, include
from . import views


urlpatterns = [
    path('menu-group/', views.MenuGroupView.as_view()),
    path('menu-group/<id>', views.MenuGroupDetailView.as_view()),
    path('all-menu-item/', views.AllMenuItemView.as_view()),
    path('menu-item/', views.MenuItemView.as_view()),
    path('menu-item/<id>', views.MenuItemDetailView.as_view()),

    path('dashboard/menu-group-count', views.menu_group_count),
    path('dashboard/menu-item-count', views.menu_item_count),
]
