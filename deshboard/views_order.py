from rest_framework import generics
from Order.models import Order,Order_Items,Shipping_Address
from Order.serializers import Order_All_Serializer,Order_Serializer


class Order_list(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_All_Serializer


class Order_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_Serializer



