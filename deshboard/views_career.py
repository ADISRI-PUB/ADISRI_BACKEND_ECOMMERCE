from Careers.models import Carrer_Job
from rest_framework import generics
from Careers.serializers import Carrer_Job_Serializer



class Carrer_List(generics.ListCreateAPIView):
    queryset = Carrer_Job.objects.all()
    serializer_class = Carrer_Job_Serializer

class Carrer_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrer_Job.objects.all()
    serializer_class = Carrer_Job_Serializer