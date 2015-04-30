from django.db import models
from django.conf import settings
import datetime

class Directory(models.Model):

    name = models.CharField(max_length=100)       
    created = models.DateTimeField()
    modified = models.DateTimeField()
    parent = models.ForeignKey("self", null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    bytes = models.IntegerField() #

    def __unicode__( self ):
        return " %s " % (self.name )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Directory, self).save(*args, **kwargs)

    def get_client_inode(self, file_set=True):
        
        data = { 
            'id':"d%s" % self.id,
            'name': self.name,
            'parent': self.parent,
            'bytes': self.bytes,
            'isDirectory': True,
            'created': self.created,
            'modified': self.modified,
        }

        if file_set:
            data['files'] = self.children()

        return data

    def children(self):

        files = File.objects.filter(parent=self)
        directories = Directory.objects.filter(parent=self)

        return [x.get_client_inode(file_set=False) for x in files or directories]


class File(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)       
    file = models.FileField(upload_to='./mediasharing/userdata/', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    parent = models.ForeignKey(Directory, null=True, blank=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    bytes = models.IntegerField(default=0)
    mime = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__( self ):
        return "(%s)" % ( self.name )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(File, self).save(*args, **kwargs)

    def get_client_inode(self, file_set=True):
        
        data = { 
            'id': "f%s" % self.id,
            'name': self.name,
            'parent': self.parent,
            'bytes': self.file.size,
            'isDirectory': False,
            'created': self.created,
            'modified': self.modified,
        }

        return data



