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
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    OrderItems_id =  models.AutoField(primary_key=True)
    Order_Items_Data = models.JSONField(null=True, blank=True,default=dict)
    Total_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)

    def _str_(self):
        return str(self.Total_Price)


class Shipping_Address(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True, blank=True)
    City=models.CharField(max_length=200,null=True, blank=True)
    PostalCode=models.CharField(max_length=200,null=True, blank=True)
    Country=models.CharField(max_length=200,null=True, blank=True)
    Shipping_Price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    Shipping_Id=models.AutoField(primary_key=True,editable=False)
    Created_At = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.City)