from django.db import models
from djmoney.models.fields import MoneyField

class Category(models.Model):
    title = models.CharField(
        verbose_name="Название"
    )
    position = models.PositiveBigIntegerField(          # Хранит !!! ТОЛЬКО !!! положительные и целые числа
        verbose_name="Позиция",
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'
        
class Product(models.Model):
    title = models.CharField(
        verbose_name="Название"
    )

    descroiption = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        null=True,
        blank=True,
        upload_to='products/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'                  
    )
    price = MoneyField(
        verbose_name="Цена",
        max_digits=12,              # Максимальное кол-во цифр
        decimal_places=2            # Знаки после запятой
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='продукт'
        verbose_name_plural='продукты'