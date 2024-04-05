from django.db import models
from django.core.validators import MinValueValidator



class PositiveFloatValidator(MinValueValidator):
    def __init__(self, message=None):
        super().__init__(0, message=message or 'Цена должна быть положительной')

class Category(models.Model):
      name = models.CharField(max_length=128,verbose_name='Название')
      description = models.CharField(max_length=1024,verbose_name='Описание')
      
      def __str__(self) -> str:
           return self.name
# Create your models here.
class Good(models.Model):
      name = models.CharField(max_length=128,verbose_name='Название')
      price = models.FloatField(validators=[PositiveFloatValidator()],verbose_name='Цена')

      category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,verbose_name='Категория')

      def __str__(self) -> str:
           return self.name
