from django.contrib import admin
from .models import Ordine, OrderItem

# Register your models here.

admin.site.register(Ordine)
admin.site.register(OrderItem)