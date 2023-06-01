from django.shortcuts import render, redirect, get_object_or_404
from .models import Prodotto
from .cart import Cart

# Create your views here.

def detail(request, pk):
    prodotto=get_object_or_404(Prodotto, pk=pk)
    context={
        "prodotto":prodotto
    }
    return render(request,'prodotti/detail.html', context )


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart=Cart(request)

    return render(request, 'prodotti/cart_view.html', {'cart':cart})

def remove_from_cart(request, product_id):
    cart=Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


