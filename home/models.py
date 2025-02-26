from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	profile_pic = models.ImageField(upload_to = "profile_pic", default = "img/profile_pic")
	
	def __str__(self):
		return self.username
		