from django.db import models
from django.urls import reverse


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})
