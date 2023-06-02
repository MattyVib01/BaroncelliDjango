from django import forms
from .models import Ordine,OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model=Ordine
        fields=('address','city','cap')