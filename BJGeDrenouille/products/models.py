from django.db import models


class Products(models.Model):
    title = models.CharField('Название', max_length=50, default='Сырок без названия')
    anons = models.CharField('Краткое описание', max_length=255, default='Сырок без краткого описания')
    description = models.TextField('Описание', default='Сырок без описания')
    manufacturer = models.CharField('Производитель', max_length=255, default='Неизвестный производитель')
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Corrected here

    def __str__(self) -> str:
        return self.title

    class Meta: 
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
