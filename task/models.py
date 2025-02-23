from django.db import models

# Create your models here.

class Task(models.Model):

	title = models.CharField(max_length = 255)
	content = models.TextField(blank = True, null = True)

	created = models.DateTimeField(auto_now = True)
	updated = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.title
