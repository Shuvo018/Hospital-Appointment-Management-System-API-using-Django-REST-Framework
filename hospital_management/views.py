from hospital_management.serializers import DoctorSerializer, AppointmentSerializer
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
        query = Doctor.objects.all()
        dept = request.query_params.get('department')
        doctor_id = request.query_params.get('doctor')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        
        if dept:
            query = query.filter(department=dept)
        elif doctor_id:
            query = query.filter(id=doctor_id)
        elif search:
            query = query.filter(name__icontains=search)
        elif ordering:
            query = query.order_by(ordering)

        serializer = DoctorSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FilterAppointmentViewAPI(APIView):
    
    def get(self, request):
        query = Appointment.objects.all()
        status = request.query_params.get('status')
        search = request.query_params.get('search')
        
        if status:
            query = query.filter(status=status)
        elif search:
            query = User.objects.filter(firstname__icontains=search)
            

        serializer = AppointmentSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)