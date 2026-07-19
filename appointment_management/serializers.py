from hospital_management.models import Doctor, User, Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at', 'updated_at']

