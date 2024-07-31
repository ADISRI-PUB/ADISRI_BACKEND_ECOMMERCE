from django.urls import path
from .views import getCarrers,getSingleCareer

urlpatterns = [
    path('',getCarrers,name="Carrers"),
    path('<str:pk>/', getSingleCareer, name='SIngleCareer'),

]