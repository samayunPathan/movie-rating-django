
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_login.urls')),
    path('',include('movie.urls')),
]
