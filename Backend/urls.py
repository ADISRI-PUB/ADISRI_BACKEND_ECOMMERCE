"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    #ADDING PATH OF APP URLS
    path('data/products/',include('Products.urls')),
    path('data/careers/',include('Careers.urls')),
    path('data/order/',include('Order.urls')),
    path('data/auth/', include('OAuth.urls')),

    #for deshboard

    path('api/product/',include('deshboard.urls_product')),
    path('api/order/',include('deshboard.urls_order')),
    path('api/user/',include('deshboard.urls_user')),
    path('api/career/',include('deshboard.urls_career')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
