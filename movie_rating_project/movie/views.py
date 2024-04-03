from django.shortcuts import render, redirect, get_object_or_404
from .models import User,  Movie, Ratings,Rating_id
from django.db.models import Q
from statistics import mean
import datetime


# Create your views here.

def get_id(type):
    ids = Rating_id.objects.all()
    if ids:
        if type == 'movie':
            return ids[0].movie_id
        elif type == 'user':
            return ids[0].user_id
        elif type == 'rating':
            return ids[0].rating_id
        else:
            return None
def update_id(type,val):
    val += 1
    ids = Rating_id.objects.all()
    if ids:
        if type == 'movie':
            ids[0].movie_id = val
            ids[0].save()
        elif type == 'user':
            ids[0].user_id = val
            ids[0].save()
        elif type == 'rating':
            ids[0].rating_id = val
            ids[0].save()
        else:
            return None
def get_average_rating(movie_id):
    try:
        return mean([current_rating.rating for current_rating in Ratings.objects.filter(movie_id=movie_id)])
    except:
        pass
def home(request):
    ratings = ['G','PG','PG-13','R','N-17']
    genre = ['Drama','Comedy','Romance','Action','Horror', 'Thriller','Crime']
    r_id = Rating_id.objects.all()
    if not r_id:
        r_id = Rating_id()
        r_id.save()
    movies = Movie.objects.all()
    all_movies= []

    for movie in movies:
        current_movie_id = movie.id
        current_movie_average_rating = get_average_rating(current_movie_id)
        all_movies.append({'id':current_movie_id,'name':str(movie.name).title(),'genre':movie.genre,'rating':movie.rating,'release_date':str(movie.release_date),'average_rating':current_movie_average_rating})
    print(all_movies)
    return render(request,'movie/home.html',{'ratings':ratings,'genre':genre,'all_movies':all_movies})

def add(request):
    if request.method == 'POST':
        name = str(request.POST.get('name')).lower()
        genre = request.POST.get('genre')
        ratings = request.POST.get('ratings')
        release_date = request.POST.get('date')
        release_date = datetime.datetime.strptime(release_date, '%m-%d-%Y').strftime('%Y-%m-%d')
        rating = request.POST.get('rate')
        movie_id = get_id('movie')
        rating_id = get_id('rating')
        try:
            new_movie = Movie(id = movie_id,name=name,genre=genre,rating=ratings,release_date=release_date)
            new_movie.save()
            update_id('movie',movie_id)
            new_rating = Ratings(id=rating_id,movie_id=new_movie,user_id = User.objects.get(id = request.session['user_id']),rating=float(rating))
            new_rating.save()
            update_id('rating',rating_id)
            return redirect('movie:home')
        except:
            pass
    return render(request, 'movie/addmovies.html', {})
def add_rating(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        rating = request.POST.get('rate')
        rating_id = get_id('rating')
        try:
            movie = Movie.objects.get(id=movie_id)
            new_rating = Ratings(id=rating_id, movie_id=movie, user_id=User.objects.get(id=request.session['user_id']),rating=float(rating))
            new_rating.save()
            return redirect('movie:home')
        
        except:
            pass

def search_movies(request):
    if request.method == 'GET':
        search_query = request.GET.get('q', '')
        if search_query:
            search_results = Movie.objects.filter(
                Q(name__icontains=search_query) | 
                Q(genre__icontains=search_query)
            )
        else:
            search_results = Movie.objects.all()
        return render(request, 'movie/search.html', {'search_results': search_results, 'search_query': search_query})