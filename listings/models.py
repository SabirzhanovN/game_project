from django.db import models
from datetime import datetime
from companies.models import Company


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Company, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=255)

    price = models.IntegerField(default=0)
    price_free = models.BooleanField(default=True)
    RAM = models.DecimalField(max_digits=2, decimal_places=1)

    support_on_windows = models.BooleanField(default=True)
    support_on_mac = models.BooleanField(default=True)
    support_on_linux = models.BooleanField(default=True)

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
