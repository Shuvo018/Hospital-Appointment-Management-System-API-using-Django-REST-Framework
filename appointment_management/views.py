from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appointment_management.serializers import AppointmentSerializer
from hospital_management.models import Appointment
from django.shortcuts import get_object_or_404
from hospital_management.permissions import IsDoctorOnly, IsPatientOnly
from rest_framework.permissions import AllowAny


class AppointmentViewAPI(APIView):

    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)

        return Response(serializer.data)
    