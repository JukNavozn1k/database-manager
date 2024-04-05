from django import forms
from . import models

class GoodForm(forms.ModelForm):
    class Meta:
        model = models.Good
        exclude = []
        widgets = {
            
            'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Крем для бритья...'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Спрос рождает предложение'}),
            'category': forms.Select(attrs={'class' : 'form-select'})
                   
        }
        labels = {
            'name' : 'Название',
            'price' : 'Цена',
            'category' : 'Категория',
        }