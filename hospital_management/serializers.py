from rest_framework import serializers
from django.contrib.auth import get_user_model
from hospital_management.models import Doctor, Appointment, User

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['name', 'department', 'specialization']

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'