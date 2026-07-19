from django.urls import path, include
from hospital_management.views import FilterDoctorViewAPI

# dashboard/
urlpatterns = [
    path('doctors/', FilterDoctorViewAPI.as_view())
]
