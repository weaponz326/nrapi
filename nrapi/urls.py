"""nrapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # personal
    path('personal-users/', include('suites.personal.users.urls')),
    path('personal-modules/portal/', include('suites.personal.modules.portal.urls')),
    path('personal-modules/settings/', include('suites.personal.modules.settings.urls')),
    path('personal-modules/calendar/', include('suites.personal.modules.calendarx.urls')),
    path('personal-modules/budget/', include('suites.personal.modules.budget.urls')),
    path('personal-modules/notes/', include('suites.personal.modules.notes.urls')),
    path('personal-modules/accounts/', include('suites.personal.modules.accountx.urls')),
    path('personal-modules/tasks/', include('suites.personal.modules.tasks.urls')),
 
    # restaurant
    path('restaurant-accounts/', include('suites.restaurant.accounts.urls')),
    path('restaurant-modules/admin/', include('suites.restaurant.modules.adminx.urls')),
    path('restaurant-modules/portal/', include('suites.restaurant.modules.portal.urls')),
    # path('restaurant-modules/settings/', include('suites.restaurant.modules.settings.urls')),
    path('restaurant-modules/menu/', include('suites.restaurant.modules.menu.urls')),
    path('restaurant-modules/staff/', include('suites.restaurant.modules.staff.urls')),
    path('restaurant-modules/payments/', include('suites.restaurant.modules.payments.urls')),
    path('restaurant-modules/orders/', include('suites.restaurant.modules.orders.urls')),
    path('restaurant-modules/kitchen_stock/', include('suites.restaurant.modules.kitchen_stock.urls')),
    path('restaurant-modules/roster/', include('suites.restaurant.modules.roster.urls')),
    path('restaurant-modules/tables/', include('suites.restaurant.modules.tables.urls')),
    path('restaurant-modules/deliveries/', include('suites.restaurant.modules.deliveries.urls')),
    path('restaurant-modules/reservations/', include('suites.restaurant.modules.reservations.urls')),
    path('restaurant-modules/customers/', include('suites.restaurant.modules.customers.urls')),
]
