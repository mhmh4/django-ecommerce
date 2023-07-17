from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
