from .models import User
from rest_framework import serializers,status 
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password  



class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=80)
    password=serializers.CharField(allow_blank=False,write_only=True)
    

    class Meta:
        model=User
        fields = ['id' ,'username', 'email', 'password']

    def validate(self, attrs): 
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")

        email_exists= User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        
        return super().validate(attrs)  

    def create(self,validated_data):
        
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user