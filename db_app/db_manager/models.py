from django.db import models
from django.core.validators import MinValueValidator



class PositiveFloatValidator(MinValueValidator):
    def __init__(self, message=None):
        super().__init__(0, message=message or 'Цена должна быть положительной')

class Category(models.Model):
      name = models.CharField(max_length=128,verbose_name='Название')

      class Meta:
           verbose_name = 'Категория'
           verbose_name_plural = 'Категории'

      def __str__(self) -> str:
           return self.name
class Good(models.Model):
      name = models.CharField(max_length=128,verbose_name='Название')
      price = models.FloatField(validators=[PositiveFloatValidator()],verbose_name='Цена')

      category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,verbose_name='Категория')

      class Meta:
           verbose_name = 'Товар'
           verbose_name_plural = 'Товары'  
      def __str__(self) -> str:
           return self.name

class Customer(models.Model):
      first_name = models.CharField(max_length=32,verbose_name='Имя')
      last_name = models.CharField(max_length=32,verbose_name='Фамилия')
      class Meta:
           verbose_name = 'Покупатель'
           verbose_name_plural = 'Покупатели'  
      def __str__(self) -> str:
           return f'{self.first_name} {self.last_name}'

class Purchase(models.Model):
      customer = models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True,verbose_name='Покупатель')
      good = models.ForeignKey('Good',on_delete=models.SET_NULL,null=True,verbose_name='Товар')
      
      class Meta:
           verbose_name = 'Покупка'
           verbose_name_plural = 'Покупки'  
      def __str__(self) -> str:
           return f'{self.first_name} {self.last_name}'
