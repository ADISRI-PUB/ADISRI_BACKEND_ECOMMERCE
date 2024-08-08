#order views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from datetime import datetime
from .models import Order,Order_Items,Shipping_Address
from .serializers import Shipping_Address_Serializer,Order_Item_Serializer,Order_Serializer,Order_All_Serializer
from Products.models  import Product
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def addOrderItems(request):
    
    user = request.user
    data = request.data
    orderItems = data['orderItems']
   
   

    if orderItems and len(orderItems)==0:
        return Response({'details':'NO OrderItems'},status=status.HTTP_400_BAD_REQUEST)

    try:    # Create a new order
            order = Order.objects.create(
                user=user,
                Tax_Price=data['TaxPrice'],
                Shipping_Price=data['ShippingPrice'],
                Total_Price=data['ToatalPrice']
            )

           

            # Create Shipping Address
            shipping = Shipping_Address.objects.create(
                order=order,

                Address=data['shippingAddress']['address'],
                City=data['shippingAddress']['city'],
                PostalCode=data['shippingAddress']['postalcode'],
                Phone_Number=data['shippingAddress']['phone'],
                School_name=data['shippingAddress']['school'],
                Shipping_Price=data['ShippingPrice'],

            )
           
            for item_data in orderItems:
                product = Product.objects.get(Product_Id=item_data['product'])
                
                item=Order_Items.objects.create(
                    product=product,
                    order=order,
                    Name=product.Name,
                    Qty=item_data['qty'],
                    Price=item_data['price'],
                    Image=item_data['image'],
                )
            product.save()
        

            serializer=Order_Serializer(order,many=False)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    except ValidationError as e:
        return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getOrderById(request, pk):
    user = request.user

    try:
        order = Order.objects.get(Order_Id=pk)

        if  order.user == user:
            serializer = Order_Serializer(order)
            return Response(serializer.data)

        else:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_401_UNAUTHORIZED)

    except Order.DoesNotExist:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def orderall(request):
    user = request.user
    try:
        orders = Order.objects.filter(user_id=user.id)
        serializer = Order_All_Serializer(orders,many=True)
        if orders:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        print(e)  # Log the exception for further debugging
        return Response({'detail': 'Error fetching orders'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
