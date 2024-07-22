from rest_framework import serializers
from .models import Carrer_Job

class Carrer_Job_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Carrer_Job
        fields = '__all__'
