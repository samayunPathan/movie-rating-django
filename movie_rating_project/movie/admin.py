from django.contrib import admin
from .models import User, Movie, Ratings
# Register your models here.


admin.site.register(Movie)
admin.site.register(Ratings)