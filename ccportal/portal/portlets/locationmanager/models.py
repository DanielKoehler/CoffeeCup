from django.db import models
from time import time


# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(height_field=10, width_field=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField()
    added = time()
    author = models.IntegerField()

  
class Photo(models.Model): 
    description = models.TextField()
    photo = models.ImageField(height_field=10, width_field=100)
    location = models.ForeignKey(Location)

