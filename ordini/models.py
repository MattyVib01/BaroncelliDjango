from django.db import models
from django.contrib.auth.models import User
from prodotti.models import Prodotto
# Create your models here.

class Ordine(models.Model):
    address=models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    cap = models.CharField(max_length=255)
    total_cost=models.IntegerField(default=0)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Ordine, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Prodotto, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)