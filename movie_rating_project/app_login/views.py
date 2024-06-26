
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import  AuthenticationForm
from .forms import SignUpForm,LoginForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            User.objects.create_user(username=username, email=email, password=password, phone=phone)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('movie:home')  # Redirect to home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'app_login/signup.html', {'form': form})

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('movie:home')
            
    return render(request, 'app_login/login.html', context={'form':form})

def user_logout(request):
    logout(request)
    return redirect('app_login:user_login')