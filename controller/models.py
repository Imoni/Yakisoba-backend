from django.db import models

class Switch(models.Model):
	host = models.CharField(unique=True, max_length=255)
	name = models.CharField(max_length=255)
	img = models.ImageField(upload_to='photos/%Y/%m/%d')
	status = models.NullBooleanField()