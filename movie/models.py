from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

class Movie(models.Model):
	title 	= models.CharField(max_length=100)
	image 	= models.ImageField(upload_to='media')
	rating 	= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
	notes	= models.TextField()

