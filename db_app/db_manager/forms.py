from django import forms
from . import models

class GoodForm(forms.ModelForm):
    class Meta:
        model = models.Good
        exclude = []
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Игровой компьютер'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'10000000000 рублей'}),
            'category': forms.Select(attrs={'class' : 'form-select'})         
        }
        labels = {
            'name' : 'Название',
            'price' : 'Цена',
            'category' : 'Категория',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        exclude = []
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Быстрое питание...'}),
        }
        labels = {
            'name' : 'Название',
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        exclude = []
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Иван'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Петров'}),
        }
        labels = {
            'first_name' : 'Имя',
            'last_name' : 'Фамилия',
        }