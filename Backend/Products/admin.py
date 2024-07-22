from django.contrib import admin

# Register your models here.
from .models import Product,Book
admin.site.register(Product)
admin.site.register(Book)
