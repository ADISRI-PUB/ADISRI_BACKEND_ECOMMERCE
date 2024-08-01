from django.urls import path
from .views import addOrderItems,getOrderById



urlpatterns = [
    path('add/', addOrderItems, name="orders-add"),
    path('<str:pk>/', getOrderById, name="user-order"),
]

