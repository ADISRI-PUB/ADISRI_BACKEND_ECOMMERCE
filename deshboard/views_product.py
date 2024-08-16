from rest_framework import generics 
from Products.models import Product ,Book
from Products.serializers import ProductSerializer,BookSerializer

class Product_list(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Product_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
