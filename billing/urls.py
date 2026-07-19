from django.urls import path, include
from billing.views import DoctorBillViewAPI,BillViewAPI

# bills/
urlpatterns = [
    path('', BillViewAPI.as_view()),
    path('doctor-bills/', DoctorBillViewAPI.as_view()),

]