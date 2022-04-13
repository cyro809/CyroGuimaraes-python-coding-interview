from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProductSerializer
from .models import Products


class ListProducts(APIView):
    pass

class ProductCreate(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductActivation(APIView):
    def get(self, request, pk, activate, format=None):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404
        if activate in ["activate", "deactivate"]:
            if activate == 'activate':
                serializer = ProductSerializer(product, data={"is_active": True})
            elif activate == 'deactivate':
                serializer = ProductSerializer(product, data={"is_active": False})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

