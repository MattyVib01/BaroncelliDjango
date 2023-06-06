from django.shortcuts import render
from prodotti.models import Categoria,Prodotto

# Create your views here.
def homepage(request):
    prodotto=Prodotto.objects.all()[0:6]
    categorie=Categoria.objects.all()
    context={
        'prodotto': prodotto,
        'categorie':categorie
    }
    return render(request, 'principale/home.html', context)



def search(request):

    if request.method=='POST':
        searched=request.POST['searched']
        context = {
            'searched': searched,
            'prodotti': Prodotto.objects.filter(nome__contains=searched)
        }
        return render(request, 'principale/search.html', context)
    else:
        return render(request, 'principale/search.html', {})
