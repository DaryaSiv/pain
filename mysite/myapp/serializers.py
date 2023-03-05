from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueTogetherValidator


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'all'