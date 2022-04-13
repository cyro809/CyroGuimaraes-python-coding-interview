from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()


    class Meta:
        model = User
        fields = '__all__'

