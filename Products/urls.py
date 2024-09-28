from django.urls import path
from .views import getProducts, getBook,getonetoeight,getRelatedBooks,getBookInThisSeries,getPamplates

urlpatterns = [
    path('product/', getProducts, name='product'),
    path('pamplates/', getPamplates, name='pamplates'),
    path('onetoeight/',getonetoeight, name='onetoeight'),
    path('relatedBook/<str:sk>/',getRelatedBooks, name='RelatedBooks'),
    path('bookseries/<str:sk>/',getBookInThisSeries, name='Book In This Series'),
    path('<str:sk>/', getBook, name='book'),
    
] 