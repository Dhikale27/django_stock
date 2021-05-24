from django import forms
from django.forms import fields
from .models import Stock


class StockForm(forms.ModelForm):  # here we use ModelForm instead of Form
    class Meta:
        model = Stock
        fields = ['ticker']
