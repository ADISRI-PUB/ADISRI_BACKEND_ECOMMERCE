from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Book
from .serializers import ProductSerializer, BookSerializer
from django.db.models import Q



@api_view(['GET'])
def getProducts(request):
    classes = request.query_params.getlist('class')
    subjects = request.query_params.getlist('subject')

    try:
        
        filters = Q()
        if classes:
            filters &= Q(Class__in=classes)
        if subjects:
            filters &= Q(Subject__in=subjects)

        products = Product.objects.filter(filters).distinct()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "No products found for the given filters."}, status=404)

@api_view(['GET'])
def getBook(request,sk):
    try:
        book = Book.objects.get(Book_Id=sk)
        serializer = BookSerializer(book,many=False)  
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "No book found with the given ID."}, status=404)
