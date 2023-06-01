from django.shortcuts import render, redirect, get_object_or_404
from .models import Prodotto

# Create your views here.

def detail(request, pk):
    prodotto=get_object_or_404(Prodotto, pk=pk)
    context={
        "prodotto":prodotto
    }
    return render(request,'prodotti/detail.html', context )




