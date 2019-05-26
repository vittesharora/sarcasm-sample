from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Question(models.Model):
	number=models.CharField(max_length=200)
	text=models.TextField()
	qimage=models.ImageField(null=True, blank=True, upload_to="media/")
    

	
	def __str__(self):
		return self.number	