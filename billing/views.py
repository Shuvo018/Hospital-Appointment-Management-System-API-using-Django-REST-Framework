from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from billing.serializers import BillSerializer
from hospital_management.models import Bill
from django.shortcuts import get_object_or_404
from hospital_management.permissions import IsDoctorOnly, IsPatientOnly
from rest_framework.permissions import AllowAny

class DoctorBillViewAPI(APIView):
    
    def get(self, request):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            bills = Bill.objects.filter(doctor=doctor_id)
            serializer = BillSerializer(bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class BillViewAPI(APIView):
    
    def get(self, request):
        patient_id = request.query_params.get('patient_id')
        if patient_id:
            bills = Bill.objects.filter(patient=patient_id)
            serializer = BillSerializer(bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    