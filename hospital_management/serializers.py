from rest_framework import serializers
from django.contrib.auth import get_user_model
from hospital_management.models import Doctor, Appointment

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['name', 'department', 'specialization']