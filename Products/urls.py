from django.urls import path
from .views import getProducts, getBook

urlpatterns = [
    path('product/', getProducts, name='product'),
    path('<str:sk>/', getBook, name='book')
]