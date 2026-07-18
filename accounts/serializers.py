from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers  import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'password', 'phone_number', 'address')