from django.urls import path, include
from .views import DoctorCreateAPIView
urlpatterns = [
    path('create/', DoctorCreateAPIView.as_view()),
]