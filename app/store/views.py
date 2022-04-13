from rest_framework.views import APIView
from .serializer import ProductSerializer
from .models import Products


class ListProducts(APIView):
    pass

class ProductCreate(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():

