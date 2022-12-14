from django.db import models
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    is_mvp = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, default=datetime.now)

    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


