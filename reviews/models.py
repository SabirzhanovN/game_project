from django.contrib.auth.models import User
from django.db import models

from listings.models import Game


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    review = models.TextField(blank=False)
    list_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
