from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    class Meta:
        model = Products
        fields = '__all__'
