from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer


class ListUsers(APIView):


    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
