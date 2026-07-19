from django.urls import path, include
from billing.views import DoctorBillViewAPI,BillViewAPI, BillDetailsViewAPI

# bills/
urlpatterns = [
    path('', BillViewAPI.as_view()),
    path('doctor-bills/', DoctorBillViewAPI.as_view()),

    path('<int:pk>/', BillDetailsViewAPI.as_view()),

]