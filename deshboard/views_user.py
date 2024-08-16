from rest_framework import generics 
from  django.contrib.auth.models import User
from OAuth.serializers import UserSerializer_Deshboard,UserSerializer

class User_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer_Deshboard

class User_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer