from django.db import models

##
# Applet Data
##
  
# class Share(models.Model): 
#     id = models.IntegerField(primary_key=True, unique=True)
#     file = models.ForeignKey('File', to_field='id')
#     directory = models.ForeignKey('Directory', to_field='id')
#     permalinkHash = models.CharField(max_length=255)
#     date = models.CharField(max_length=255)
  
# class Directory(models.Model): 
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     parent = models.ForeignKey('Directory', to_field='id')
#     owner = models.ForeignKey('User', to_field='id')

# class FileReference(models.Model): 
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length=255)
#     resourceHash = models.CharField(max_length=255)
#     hostRootPath = models.CharField(max_length=255)
#     networkHost = models.CharField(max_length=255)

  
# class File(models.Model): 
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length=255)
#     mimeType = models.CharField(max_length=255)
#     parent = models.ForeignKey('Directory', to_field='id')
#     locationReference = models.ForeignKey('FileReference', to_field='id')

# ##
# # Ownership 
# ##

# class DirectoryUserGroup(models.Model): 
#     did = models.ForeignKey('Directory', to_field='id')
#     uid = models.ForeignKey('User', to_field='id')
#     shared = models.DateTimeField()
 
  
# class DirectoryUser(models.Model): 
#     did = models.ForeignKey('Directory', to_field='id')
#     ugid = models.ForeignKey('UserGroup', to_field='id')
#     shared = models.DateTimeField()