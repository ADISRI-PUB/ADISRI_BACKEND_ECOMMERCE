from django.contrib import admin

# Register your models here.
from .models import Order,Order_Items,Shipping_Address

admin.site.register(Order)
admin.site.register(Order_Items)
admin.site.register(Shipping_Address)