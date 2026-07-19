from hospital_management.models import Bill
from rest_framework import serializers

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['patient', 'doctor', 'appointment', 'consultation_fee', 'discount', 'total_amount']