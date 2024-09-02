from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Book
from .serializers import ProductSerializer, BookSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def getonetoeight(request):
    classes = request.query_params.getlist('class')
    subjects = request.query_params.getlist('subject')

    try:
        
        filters = Q()
        if classes:
            filters &= Q(Class__in=classes)
        if subjects:
            filters &= Q(Subject__in=subjects)

        products = Product.objects.filter(filters).distinct().exclude(Class__in=["Play","Nursery","Pre - Primer","Primer"]).order_by('Product_Id')
        # Pagination
        paginator =PageNumberPagination()
        paginator.page_size =10
        paginated_products = paginator.paginate_queryset(products, request)
        
        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "No products found for the given filters."}, status=404)




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

        products = Product.objects.filter(filters).distinct().exclude(Class__in=[1,2,3,4,5]).order_by('Product_Id')
         # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # You can set this to a different value or configure globally
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)
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
