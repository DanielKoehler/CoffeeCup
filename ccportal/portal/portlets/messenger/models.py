from django.db import models
from django.conf import settings

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)    
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='./messenger/threads/', null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_message = models.DateTimeField(null=True, blank=True)

    def __unicode__( self ):
        return "Thread ID: %d (%s)" % (self.id, ", ".join([u.get_full_name() for u in self.users.all()]))

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    thread = models.ForeignKey(Thread)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__( self ):
        return "Message ID: %d (%s)" % (self.id, self.get_excerp())

    def get_excerp(self, length=24):
        if len(self.text) < length:
            return self.text
        return "%s..." % self.text[:length - 3] 

class Attachment(models.Model):
    content = models.FileField(upload_to='./messenger/attachments/')
    message = models.ForeignKey(Message)