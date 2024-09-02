from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import os

def product_image_upload_path(instance, filename):
    product_name = slugify(instance.Name)
    return os.path.join('Products', product_name, filename)

def book_image_upload_path(instance, filename):
    book_name = slugify(instance.Name)
    return os.path.join('Books', book_name, filename)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Product_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, null=False, blank=False)
    Subject = models.CharField(max_length=200, null=False, blank=False)
    Class = models.CharField(max_length=20, null=True, blank=True)
    Price = models.IntegerField(null=False, blank=False)
    Image = models.ImageField(upload_to=product_image_upload_path)
    Create_Date_At=models.DateField(auto_now_add=True, null=True, blank=True)
    Create_Time_At=models.TimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.Name


class Book(models.Model):
    Book_Id = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='book_detail')
    Description = models.TextField(null=True, blank=True)
    Page = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=False, blank=False, default=0)
    Name = models.CharField(max_length=200, null=False, blank=False)
    Subject = models.CharField(max_length=20, null=False, blank=False)
    Class = models.CharField(max_length=20, null=False, blank=False)
    Author = models.CharField(max_length=100, null=True, blank=True)
    Publication = models.CharField(max_length=100, null=False, blank=False)
    Isbn = models.CharField(max_length=20, null=True, blank=True)
    Cover_Image = models.ImageField(upload_to=book_image_upload_path,null=False, blank=False)#1
    Back_Image = models.ImageField(upload_to=book_image_upload_path,null=True , blank=True)#2
    Index_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)#3
    Page1_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page2_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page3_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page4_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page5_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page6_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page7_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page8_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page9_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page10_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page11_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page12_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page13_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page14_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page15_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page16_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)
    Page17_Image = models.ImageField(upload_to=book_image_upload_path,null=True, blank=True)

    Create_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name



