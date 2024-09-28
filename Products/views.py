from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Book,Pamplate
from .serializers import ProductSerializer, BookSerializer,PamplateSerializer
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

        paginator =PageNumberPagination()
        paginator.page_size =20
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
        paginator = PageNumberPagination()
        paginator.page_size = 20 
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "No products found for the given filters."}, status=404)


@api_view(['GET'])
def getPamplates(request):

    pamplates = request.query_params.getlist('pamplates')

    try:
        
        filters = Q()
        if pamplates:
            filters &= Q(Name__in=pamplates)
        products = Pamplate.objects.filter(filters)
        serializer = PamplateSerializer(products, many=True)
        return Response(serializer.data)
    except Pamplate.DoesNotExist:
        return Response({"error": "No Pamplate found for the given filters."}, status=404)



@api_view(['GET'])
def getBook(request,sk):
    try:
        sk=sk.replace("+"," ")
        sk=sk.split("product_id")
        
        book = Book.objects.get(Book_Id=sk[1])
        serializer = BookSerializer(book,many=False)  
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "No book found with the given ID."}, status=404)



# Related Books Api
@api_view(['GET'])
def getRelatedBooks(request,sk):
    try:
        sk=sk[0].upper()+sk[1::]
        book = Product.objects.filter(Class=sk)
        serializer = ProductSerializer(book,many=True)
        return  Response(serializer.data)
    except :
        return Response({"error": "No book found with the given Class."}, status=404)



# Book In This Series
@api_view(['GET'])
def getBookInThisSeries(request,sk):
    try:

        sk=sk.replace("+"," ")
        sk=sk.split("product_id")
        book = Product.objects.get(Product_Id=sk[1])
        Products=Product.objects.filter(Series=book.Series).exclude(Product_Id=sk[1])
        if book.Class in ['Play','Primer','Pre - Primer','Nursery'] :  
            Products=Products.exclude(Class__in =[1,2,3,4,5])
        else: 
            Products=Products.exclude(Class__in =['Play','Primer','Pre - Primer','Nursery'])
        serializer = ProductSerializer(Products,many=True)
        return  Response(serializer.data)
    except :
        return Response({"error": "No book found with the given Subject."}, status=404)

     