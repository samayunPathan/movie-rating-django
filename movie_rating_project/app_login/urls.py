from django.urls import path
from app_login import views

app_name='app_login'


urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="user_login"),
]
