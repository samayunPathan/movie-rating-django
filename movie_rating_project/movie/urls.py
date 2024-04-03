from django.urls import path
from movie import views

app_name='movie'


urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('search/',views.search_movies,name='search'),
    path('search/<id>',views.search_movies,name='search_id'),
    path('addrating/',views.add_rating,name='addrating'),
]
