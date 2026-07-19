from django.urls import path, include
from hospital_management.views import FilterDoctorViewAPI, FilterAppointmentViewAPI

# dashboard/
urlpatterns = [
    path('doctors/', FilterDoctorViewAPI.as_view()),
    path('appointments/', FilterAppointmentViewAPI.as_view()),
]
