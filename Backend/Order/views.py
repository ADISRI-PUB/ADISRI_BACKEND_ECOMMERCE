#order views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from datetime import datetime
from .models import Order,Order_Items,Shipping_Address
from .serializers import Shipping_Address_Serializer,Order_Item_Serializer,Order_Serializer
from Products.models  import Product
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def addOrderItems(request):
    
    user = request.user
    data = request.data
    orderItems = data.get('orderItems', [])

    if orderItems and len(orderItems)==0:
        return Response({'details':'NO OrderItems'},status=status.HTTP_400_BAD_REQUEST)

    try:    # Create a new order
            order = Order.objects.create(
                user=user,
                Tax_Price=data.get('Tax_Price'),
                Shipping_Price=data.get('Shipping_Price'),
                Total_Price=data.get('Total_Price'),
            )

            # Create Shipping Address
            shipping_data = data.get('Shipping_Address', {})
            shipping = Shipping_Address.objects.create(
                order=order,
                Address=shipping_data.get('Address'),
                City=shipping_data.get('City'),
                PostalCode=shipping_data.get('PostalCode'),
                Country=shipping_data.get('Country'),
                Shipping_Price=shipping_data.get('Shipping_Price'),
            )

            # Create Order Items and set order to orderitem relationship
            for item_data in orderItems:
                # Create Order_Items instance
                order_item = Order_Items.objects.create(
                    order=order,
                    Total_Price=item_data.get('Total_Price'),
                    Order_Items_Data=item_data.get('Order_Items_Data'),
                )
                
                # Add products to Order_Items through ManyToMany relationship
                products_data = item_data.get('products', [])  # Assuming 'products' is a list of product IDs
                products = Product.objects.filter(id__in=products_data)
                order_item.product.add(*products)  # Adding products to the ManyToManyField

            serializer = Order_Serializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getOrderById(request, pk):
    user = request.user

    try:
        order = Order.objects.get(Order_Id=pk)

        if user.is_staff or order.user == user:
            serializer = Order_Serializer(order)
            return Response(serializer.data)

        else:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_401_UNAUTHORIZED)

    except Order.DoesNotExist:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)