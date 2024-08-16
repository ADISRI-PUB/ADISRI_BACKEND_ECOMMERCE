from django.urls import path
from .views_career import Carrer_List,Carrer_Detail

urlpatterns = [
    path('',Carrer_List.as_view(),name='Careers'),
    path('<int:pk>/',Carrer_Detail.as_view(),name='Careers-Detail')
]