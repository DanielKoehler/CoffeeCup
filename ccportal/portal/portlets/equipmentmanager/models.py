from django.db import models
from time import time
from django.conf import settings

import locationmanager

class EquipmentItem(models.Model):
    title = models.CharField(max_length=255)
    shortTitle = models.CharField(max_length=255)
    insurance = models.CharField(max_length=255)
    description = models.TextField()
    added = time()
    location = models.ForeignKey('locationmanager.Location')

class ItemHistory(models.Model): 
    description = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    item = models.ForeignKey(EquipmentItem)
    time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)