from django.urls import path, include
from appointment_management.views import AppointmentViewAPI

# appointments/
urlpatterns = [
    path('', AppointmentViewAPI.as_view(), name='appointment-list'),
]
