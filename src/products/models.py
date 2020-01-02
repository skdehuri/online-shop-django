from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    summary = models.TextField()
    featured = models.BooleanField(default=True)
