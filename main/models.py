from django.db import models


class Drug(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField()
