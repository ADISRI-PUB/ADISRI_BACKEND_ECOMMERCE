from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializerWithToken,MyTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from  django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer =UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]= v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user =request.user
    serializer=UserSerializer(user)
    return Response(serializer.data)



@api_view(['POST'])
def registerUser(request):
    data = request.data
    k=User.objects.filter(first_name=data['name'])
    if(len(k)== 1):
        return Response("User with this email already exists")

    else:
        user =User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password']))
        serializer=UserSerializerWithToken(user,many=False)
        return Response(serializer.data)