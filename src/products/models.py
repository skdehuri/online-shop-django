from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    summary = models.TextField()
    featured = models.BooleanField(default=True)

    class Meta:
        db_table = 'tbl_products'

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'id': self.id})  # f'product/{self.id}'
