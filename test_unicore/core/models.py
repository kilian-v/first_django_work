from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    number = models.CharField(max_length=200, null=False)
    timetables = models.CharField(max_length=200, null=False)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })
