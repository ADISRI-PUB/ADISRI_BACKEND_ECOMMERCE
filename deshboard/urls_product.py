from django.urls import path
from .views_product import Product_Detail,Product_list

urlpatterns = [
    path('',Product_list.as_view(),name='Product- list'),
    path('<int:pk>/',Product_Detail.as_view(),name='Product- detail'),
]