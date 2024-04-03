from django.urls import path
from app_login import views

app_name='app_login'


urlpatterns = [
    path('login/',views.user_login,name="user_login"),
]
