from .models import User
from rest_framework import serializers 



class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=80)
   
    password= serializers.CharField(min_length=8)

    class Meta:
        model=User
        fields = ['username', 'email', 'password', 'phone_number']

    def validate(self, attrs): 
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")

        email_exists= User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(detail="User with phonenumber exists")

        return super().validate(attrs)  