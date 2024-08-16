from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return {key : value for key , value in representation.items() if value not in[None,'',[],{}]}

