from django.shortcuts import render, redirect, get_object_or_404
from .models import Prodotto, Categoria
from .cart import Cart

# Create your views here.

def detail(request, pk):
    prodotto=get_object_or_404(Prodotto, pk=pk)
    context={
        "prodotto":prodotto
    }
    return render(request,'prodotti/detail.html', context )


def category(request, pk):
    prod_categoria=Prodotto.objects.filter(categoria=pk)
    categoria=Categoria.objects.get(pk=pk)
    context={
        'prod_categoria':prod_categoria,
        'categoria': categoria
    }
    return render(request, 'prodotti/category.html', context )

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


def change_quantity(request, product_id):
    action=request.GET.get('action','')
    if action:
        quantity=1

        if action=='decrease':
            quantity=-1
        cart=Cart(request)
        cart.add(product_id,quantity,True)

    return redirect('cart_view')


