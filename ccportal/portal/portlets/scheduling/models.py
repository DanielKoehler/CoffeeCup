from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)    

    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    groups = models.ManyToManyField(Group)
    
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def as_json(self):
    	return dict (
    		    title = self.title,    
			    latitude = self.latitude,
			    longitude = self.longitude,
			    start = self.start,
			    end = self.end,
			    url= "/scheduler/event/%s" % self.id
    		)
