from rest_framework.generics import ListAPIView, GenericAPIView
from .serializers import  PublisherSerializer
from rest_framework.generics import ListAPIView

from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
# class ServicesListView(ListAPIView):
#     model = 


# class LoginAPI(generics.GenericAPIView):
#     serializer_class = CustomUserSerializer

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response({'error': 'Invalid credentials'})
#         return Response({
#             "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
#             "token": Token.objects.create(user=user).key
#         })

class PublisherView(ListAPIView):
    serializer_class = PublisherSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]