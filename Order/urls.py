from django.urls import path
from .views import addOrderItems,getOrderById,orderall



urlpatterns = [
    path('all/',orderall , name="user-all-order"),
    path('add/', addOrderItems, name="orders-add"),
    path('<str:pk>/', getOrderById, name="user-order"),
]

