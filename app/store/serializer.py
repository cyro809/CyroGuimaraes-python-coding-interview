from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    class Meta:
        model = Products
        fields = '__all__'
