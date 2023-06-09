"""BaroncelliDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from principale.views import homepage,search
from prodotti.views import detail, add_to_cart, cart_view, remove_from_cart, change_quantity, category
from register.views import register
from ordini.views import checkout,my_orders



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='home'),
    path('<int:pk>',detail, name='detail'),
    path('category/<int:pk>', category, name='category' ),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('search/', search, name='search'),
    path('add-to-cart/<int:product_id>/', add_to_cart,name='add-to-cart'),
    path('cart/',cart_view, name='cart_view'),
    path('remove-from-cart/<int:product_id>/',remove_from_cart,name='remove_from_cart'),
    path('change-quantity/<int:product_id>/', change_quantity, name='change_quantity'),
    path('cart/checkout/',checkout,name='checkout'),
    path('myorders/', my_orders, name='my_orders'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
