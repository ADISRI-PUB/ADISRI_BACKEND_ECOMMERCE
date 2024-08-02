
#order models.py
from django.db import models
from django.contrib.auth.models import User
from Products.models import Product


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    Order_Id = models.AutoField(primary_key=True)
    Tax_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Shipping_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Total_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Is_Delivered=models.BooleanField(default=False)
    Delivered_At=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    CreateAt=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.CreateAt)


class Order_Items(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    Name=models.CharField(max_length=200,null=True, blank=True)
    Qty=models.IntegerField(null=True, blank=True,default=0)
    Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Image=models.CharField(max_length=200,null=True, blank=True)
    OrderItem_id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.Name)


class Shipping_Address(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True, blank=True)
    City=models.CharField(max_length=200,null=True, blank=True)
    PostalCode=models.CharField(max_length=200,null=True, blank=True)
    Phone_Number=models.CharField(max_length=10,null=True, blank=True)
    School_name=models.CharField(max_length=200,null=True, blank=True)
    Shipping_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Shipping_Id=models.AutoField(primary_key=True,editable=False)
    Created_At = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.City)


