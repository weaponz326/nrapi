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
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('payments/', include('suites.personal.payments.urls')),
    path('support/', include('suites.personal.support.urls')),

    # personal
    path('personal-users/', include('suites.personal.users.urls')),
    path('personal-modules/portal/', include('suites.personal.modules.portal.urls')),
    path('personal-modules/settings/', include('suites.personal.modules.settings.urls')),
    path('personal-modules/calendar/', include('suites.personal.modules.calendar.urls')),
    path('personal-modules/budget/', include('suites.personal.modules.budget.urls')),
    path('personal-modules/notes/', include('suites.personal.modules.notes.urls')),
    path('personal-modules/accounts/', include('suites.personal.modules.accounts.urls')),
    path('personal-modules/tasks/', include('suites.personal.modules.tasks.urls')),
     
    # restaurant
    path('restaurant-accounts/', include('suites.restaurant.accounts.urls')),
    path('restaurant-modules/admin/', include('suites.restaurant.modules.admin.urls')),
    path('restaurant-modules/portal/', include('suites.restaurant.modules.portal.urls')),
    path('restaurant-modules/settings/', include('suites.restaurant.modules.settings.urls')),
    path('restaurant-modules/menu/', include('suites.restaurant.modules.menu.urls')),
    path('restaurant-modules/staff/', include('suites.restaurant.modules.staff.urls')),
    path('restaurant-modules/payments/', include('suites.restaurant.modules.payments.urls')),
    path('restaurant-modules/orders/', include('suites.restaurant.modules.orders.urls')),
    path('restaurant-modules/kitchen-stock/', include('suites.restaurant.modules.kitchen_stock.urls')),
    path('restaurant-modules/roster/', include('suites.restaurant.modules.roster.urls')),
    path('restaurant-modules/tables/', include('suites.restaurant.modules.tables.urls')),
    path('restaurant-modules/deliveries/', include('suites.restaurant.modules.deliveries.urls')),
    path('restaurant-modules/reservations/', include('suites.restaurant.modules.reservations.urls')),
    path('restaurant-modules/customers/', include('suites.restaurant.modules.customers.urls')),

    # school
    path('school-accounts/', include('suites.school.accounts.urls')),
    path('school-modules/admin/', include('suites.school.modules.admin.urls')),
    path('school-modules/portal/', include('suites.school.modules.portal.urls')),
    path('school-modules/settings/', include('suites.school.modules.settings.urls')),
    path('school-modules/parents/', include('suites.school.modules.parents.urls')),
    path('school-modules/assessment/', include('suites.school.modules.assessment.urls')),
    path('school-modules/subjects/', include('suites.school.modules.subjects.urls')),
    path('school-modules/attendance/', include('suites.school.modules.attendance.urls')),
    path('school-modules/students/', include('suites.school.modules.students.urls')),
    path('school-modules/lesson-plan/', include('suites.school.modules.lesson_plan.urls')),
    path('school-modules/reports/', include('suites.school.modules.reports.urls')),
    path('school-modules/teachers/', include('suites.school.modules.teachers.urls')),
    path('school-modules/payments/', include('suites.school.modules.payments.urls')),
    path('school-modules/terms/', include('suites.school.modules.terms.urls')),
    path('school-modules/classes/', include('suites.school.modules.classes.urls')),
    path('school-modules/timetable/', include('suites.school.modules.timetable.urls')),
    path('school-modules/fees/', include('suites.school.modules.fees.urls')),
    path('school-modules/sections/', include('suites.school.modules.sections.urls')),

    # association
    path('association-accounts/', include('suites.association.accounts.urls')),
    path('association-modules/admin/', include('suites.association.modules.admin.urls')),
    path('association-modules/portal/', include('suites.association.modules.portal.urls')),
    path('association-modules/settings/', include('suites.association.modules.settings.urls')),
    path('association-modules/accounts/', include('suites.association.modules.accounts.urls')),
    path('association-modules/members/', include('suites.association.modules.members.urls')),
    path('association-modules/committees/', include('suites.association.modules.committees.urls')),
    path('association-modules/dues/', include('suites.association.modules.dues.urls')),
    path('association-modules/executives/', include('suites.association.modules.executives.urls')),
    path('association-modules/action-plan/', include('suites.association.modules.action_plan.urls')),
    path('association-modules/attendance/', include('suites.association.modules.attendance.urls')),
    path('association-modules/meetings/', include('suites.association.modules.meetings.urls')),
    path('association-modules/groups/', include('suites.association.modules.groups.urls')),
    path('association-modules/fiscal-year/', include('suites.association.modules.fiscal_year.urls')),

    # enterprise
    path('enterprise-accounts/', include('suites.enterprise.accounts.urls')),
    path('enterprise-modules/admin/', include('suites.enterprise.modules.admin.urls')),
    path('enterprise-modules/portal/', include('suites.enterprise.modules.portal.urls')),
    path('enterprise-modules/settings/', include('suites.enterprise.modules.settings.urls')),
    path('enterprise-modules/accounts/', include('suites.enterprise.modules.accounts.urls')),
    path('enterprise-modules/appraisal/', include('suites.enterprise.modules.appraisal.urls')),
    path('enterprise-modules/assets/', include('suites.enterprise.modules.assets.urls')),
    path('enterprise-modules/attendance/', include('suites.enterprise.modules.attendance.urls')),
    path('enterprise-modules/budget/', include('suites.enterprise.modules.budget.urls')),
    path('enterprise-modules/employees/', include('suites.enterprise.modules.employees.urls')),
    path('enterprise-modules/files/', include('suites.enterprise.modules.files.urls')),
    path('enterprise-modules/fiscal-year/', include('suites.enterprise.modules.fiscal_year.urls')),
    path('enterprise-modules/leave/', include('suites.enterprise.modules.leave.urls')),
    path('enterprise-modules/ledger/', include('suites.enterprise.modules.ledger.urls')),
    path('enterprise-modules/letters/', include('suites.enterprise.modules.letters.urls')),
    path('enterprise-modules/payroll/', include('suites.enterprise.modules.payroll.urls')),
    path('enterprise-modules/procurement/', include('suites.enterprise.modules.procurement.urls')),
    path('enterprise-modules/reception/', include('suites.enterprise.modules.reception.urls')),

    # hotel
    path('hotel-accounts/', include('suites.hotel.accounts.urls')),
    path('hotel-modules/admin/', include('suites.hotel.modules.admin.urls')),
    path('hotel-modules/portal/', include('suites.hotel.modules.portal.urls')),
    path('hotel-modules/settings/', include('suites.hotel.modules.settings.urls')),
    path('hotel-modules/bills/', include('suites.hotel.modules.bills.urls')),
    path('hotel-modules/staff/', include('suites.hotel.modules.staff.urls')),
    path('hotel-modules/roster/', include('suites.hotel.modules.roster.urls')),
    path('hotel-modules/guests/', include('suites.hotel.modules.guests.urls')),
    path('hotel-modules/payments/', include('suites.hotel.modules.payments.urls')),
    path('hotel-modules/services/', include('suites.hotel.modules.services.urls')),
    path('hotel-modules/checkin/', include('suites.hotel.modules.checkin.urls')),
    path('hotel-modules/bookings/', include('suites.hotel.modules.bookings.urls')),
    path('hotel-modules/rooms/', include('suites.hotel.modules.rooms.urls')),
    path('hotel-modules/assets/', include('suites.hotel.modules.assets.urls')),
    path('hotel-modules/housekeeping/', include('suites.hotel.modules.housekeeping.urls')),

    # hospital
    path('hospital-accounts/', include('suites.hospital.accounts.urls')),
    path('hospital-modules/admin/', include('suites.hospital.modules.admin.urls')),
    path('hospital-modules/portal/', include('suites.hospital.modules.portal.urls')),
    path('hospital-modules/settings/', include('suites.hospital.modules.settings.urls')),
    path('hospital-modules/patients/', include('suites.hospital.modules.patients.urls')),
    path('hospital-modules/appointments/', include('suites.hospital.modules.appointments.urls')),
    path('hospital-modules/staff/', include('suites.hospital.modules.staff.urls')),
    path('hospital-modules/bills/', include('suites.hospital.modules.bills.urls')),
    path('hospital-modules/doctors/', include('suites.hospital.modules.doctors.urls')),
    path('hospital-modules/laboratory/', include('suites.hospital.modules.laboratory.urls')),
    path('hospital-modules/payments/', include('suites.hospital.modules.payments.urls')),
    path('hospital-modules/nurses/', include('suites.hospital.modules.nurses.urls')),
    path('hospital-modules/prescriptions/', include('suites.hospital.modules.prescriptions.urls')),
    path('hospital-modules/diagnosis/', include('suites.hospital.modules.diagnosis.urls')),
    path('hospital-modules/drugs/', include('suites.hospital.modules.drugs.urls')),
    path('hospital-modules/wards/', include('suites.hospital.modules.wards.urls')),
    path('hospital-modules/admissions/', include('suites.hospital.modules.admissions.urls')),
    path('hospital-modules/dispensary/', include('suites.hospital.modules.dispensary.urls')),
    path('hospital-modules/roster/', include('suites.hospital.modules.roster.urls')),

    # shop
    path('shop-accounts/', include('suites.shop.accounts.urls')),
    path('shop-modules/admin/', include('suites.shop.modules.admin.urls')),
    path('shop-modules/portal/', include('suites.shop.modules.portal.urls')),
    path('shop-modules/settings/', include('suites.shop.modules.settings.urls')),
    path('shop-modules/receivables/', include('suites.shop.modules.receivables.urls')),
    path('shop-modules/products/', include('suites.shop.modules.products.urls')),
    path('shop-modules/invoice/', include('suites.shop.modules.invoice.urls')),
    path('shop-modules/marketting/', include('suites.shop.modules.marketting.urls')),
    path('shop-modules/payables/', include('suites.shop.modules.payables.urls')),
    path('shop-modules/sales/', include('suites.shop.modules.sales.urls')),
    path('shop-modules/customers/', include('suites.shop.modules.customers.urls')),
    path('shop-modules/payments/', include('suites.shop.modules.payments.urls')),
    path('shop-modules/orders/', include('suites.shop.modules.orders.urls')),
    path('shop-modules/inventory/', include('suites.shop.modules.inventory.urls')),
    path('shop-modules/suppliers/', include('suites.shop.modules.suppliers.urls')),
    path('shop-modules/purchasing/', include('suites.shop.modules.purchasing.urls')),
    path('shop-modules/cashflow/', include('suites.shop.modules.cashflow.urls')),
    path('shop-modules/staff/', include('suites.shop.modules.staff.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
