from django.urls import path
from .views_user import User_list,User_Detail

urlpatterns = [
    path('',User_list.as_view(),name='user-list'),
    path('<int:pk>/',User_Detail.as_view(),name='user-detail'),
]