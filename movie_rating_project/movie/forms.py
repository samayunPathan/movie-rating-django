from django import forms
from .models import *

#movie add form

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'genre', 'movie_logo', 'release_date')