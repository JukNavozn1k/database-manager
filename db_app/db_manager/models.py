from django.db import models
from django.core.validators import MinValueValidator



class PositiveFloatValidator(MinValueValidator):
    def __init__(self, message=None):
        super().__init__(0, message=message or 'Цена должна быть положительной')

class Category(models.Model):
      name = models.CharField(max_length=128,unique=True)
      description = models.CharField(max_length=1024)
      
      def __str__(self) -> str:
           return self.name
# Create your models here.
class Good(models.Model):
      name = models.CharField(max_length=128,unique=True)
      price = models.FloatField(validators=[PositiveFloatValidator()])

      category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

      def __str__(self) -> str:
           return self.name
