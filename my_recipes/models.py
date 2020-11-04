from django.db import models

# Create your models here.



class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=False)
    image_url = models.URLField(blank=False)
    description = models.TextField(blank=False)
    ingredients = models.CharField(max_length=250, blank=False, )
    time = models.PositiveIntegerField(blank=False, default=0)


