from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from app_login.models import User

# Create your models here.


class Movie(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=100,blank=True)
    genre = models.CharField(max_length=100,blank=True)
    rating = models.CharField(max_length=10,blank=True)
    release_date = models.DateField(blank=True)

    def __str__(self):
        return self.name

class Ratings(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    def __str__(self):
        return f"{self.user_id.name} rated {self.movie_id.name} {self.rating}"
class Rating_id(models.Model):
    user_id = models.IntegerField(default=1)
    movie_id = models.IntegerField(default=1)
    rating_id = models.IntegerField(default=1)