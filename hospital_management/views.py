from hospital_management.serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hospital_management.models import Doctor, User, Appointment
from django.shortcuts import get_object_or_404
from hospital_management.permissions import IsDoctorOnly
from rest_framework.permissions import AllowAny

# Create your views here.


class FilterDoctorViewAPI(APIView):
    
    def get(self, request):
        dept = request.query_params.get('department')
        doctor_id = request.query_params.get('doctor')
        
        if dept:
            query = Doctor.objects.filter(department=dept)
        elif doctor_id:
            query = Doctor.objects.filter(id=doctor_id)

        serializer = DoctorSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FilterAppointmentViewAPI(APIView):
    
    def get(self, request):
        status = request.query_params.get('status')
        search = request.query_params.get('search')
        
        if status:
            query = Appointment.objects.filter(status=status)
        elif search:
            query = User.objects.filter(name=search)

        serializer = DoctorSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)