from django.urls import path
from .views import addOrderItems,getOrderById,orderall,delete_order



urlpatterns = [
    path('all/',orderall , name="user-all-order"),
    path('add/', addOrderItems, name="orders-add"),
    path('<str:pk>/', getOrderById, name="user-order"),
    path('delete/<str:pk>/', delete_order, name="delete-order"),

]

