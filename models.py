from django.db import models

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=200)
	link = models.URLField()
	published = models.DateTimeField()
	source = models.CharField(max_length=200)
