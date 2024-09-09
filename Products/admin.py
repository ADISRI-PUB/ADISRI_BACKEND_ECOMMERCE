from django.contrib import admin

# Register your models here.
from .models import Product,Book,Pamplates
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Pamplates)