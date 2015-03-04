from django.db import models

# Create your models here.

class User(models.Model):



	"""docstring for UserAuth"""
	def __init__(self, arg):
		super(UserAuth, self).__init__()
		self.arg = arg
		