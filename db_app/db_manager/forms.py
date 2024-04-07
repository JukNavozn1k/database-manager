from django import forms
from . import models

class GoodForm(forms.ModelForm):
    class Meta:
        model = models.Good
        exclude = []
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Название товара'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Цена товара'}),
            'category': forms.Select(attrs={'class' : 'form-select'})         
        }
        labels = {
            'name' : 'Название',
            'price' : 'Цена',
            'category' : 'Категория',
        }