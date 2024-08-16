from django.urls import path
from .views_order import Order_list,Order_Details

urlpatterns = [
    path('',Order_list.as_view(),name='Order-List'),
    path('<int:pk>/',Order_Details.as_view(),name='Orderdeatil'),
]