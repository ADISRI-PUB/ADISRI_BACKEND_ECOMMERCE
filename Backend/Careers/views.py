from django.shortcuts import render
from .models import Carrer_Job
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Carrer_Job_Serializer




# Create your views here.
@api_view(['GET'])
def getCarrers(request):
    carrer=Carrer_Job.objects.all()
    serializer=Carrer_Job_Serializer(carrer,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleCareer(request,pk):
    carrer=Carrer_Job.objects.get(Carrer_Job_Id=pk)
    serializer=Carrer_Job_Serializer(carrer,many=False)
    return Response(serializer.data)