from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()


    class Meta:
        model = User
        fields = ('name', 'age')

