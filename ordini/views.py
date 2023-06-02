from django.shortcuts import render, redirect
from prodotti.cart import Cart
from .forms import OrderForm
from .models import Ordine, OrderItem



# Create your views here.

def checkout(request):
    cart=Cart(request)

    if request.method == 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.created_by=request.user
            order.save()

            for item in cart:
                product=item['product']
                quantity = int(item['quantity'])
                price = product.prezzo * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()
            return redirect('home')
    else:
        form=OrderForm()
    context={
        'cart':cart,
        'form':form,
    }
    return render(request,'ordini/checkout.html', context)


def my_orders(request):
        order=Ordine.objects.filter(created_by__username=request.user)
        orderitems=OrderItem.objects.filter(order__created_by__username=request.user)
        context={
            'order':order,
            'orderitems':orderitems,
        }
        return render(request,'ordini/myorders.html', context)
