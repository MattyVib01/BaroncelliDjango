from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    titolo=models.CharField(max_length=30)

    class Meta:
        verbose_name_plural='Categorie'

    def __str__(self):
        return self.titolo

class Prodotto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome=models.CharField(max_length=30)
    descrizione=models.TextField(blank=True, null=True)
    prezzo=models.DecimalField(max_digits=7,decimal_places=2)
    immagine=models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome




    class Meta:
        verbose_name_plural='Prodotti'




class Carrello(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    prodotti=models.ManyToManyField('Prodotto', through='ProdottoCarrello')

    def __str__(self):
        return f'Carrello di {self.user.username}'

class ProdottoCarrello(models.Model):
    carrello=models.ForeignKey(Carrello, on_delete=models.CASCADE)
    prodotto=models.ForeignKey(Prodotto,on_delete=models.CASCADE)
    quantità=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantità}x{self.prodotto.nome}'




