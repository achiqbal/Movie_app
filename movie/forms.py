from django import forms
from .models import Movie
from PIL import Image

class CreateMovie(forms.ModelForm):
	image = forms.ImageField()
	class Meta:
		model = Movie
		fields = ['title', 'image', 'rating', 'notes']