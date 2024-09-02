from django.urls import path
from .views import getProducts, getBook,getonetoeight

urlpatterns = [
    path('product/', getProducts, name='product'),
    path('onetoeight/',getonetoeight, name='onetoeight'),
    path('<str:sk>/', getBook, name='book'),
    
]