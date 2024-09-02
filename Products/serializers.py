from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Book
from django.db.models import ImageField

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    Image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ["Cover_Image","Back_Image","Index_Image","Page1_Image","Page2_Image","Page3_Image","Page4_Image","Page5_Image","Page6_Image","Page7_Image","Page8_Image","Page9_Image","Page10_Image","Page11_Image","Page12_Image","Page13_Image","Page14_Image","Page15_Image","Page16_Image","Page17_Image"]
    
    def get_Image(self,obj):
        all_fields = obj._meta.get_fields()
        image_fields =[field.name for field in all_fields if isinstance(field,ImageField)]
        images = [ getattr(obj, field).url for field in image_fields if getattr(obj, field)]
        return images
        

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return {key : value for key , value in representation.items() if value not in[None,'',[],{}]}

