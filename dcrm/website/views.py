from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.POST:
        email = request.POST['email'] # check home.html label input names for login form
        password = request.POST['password'] # check home.html label input names for login form
        # Authenticate
        user = authenticate(request, email=email, password = password)
        if user: # if doesn't work add is not None after user
            login(request, user)
            messages.success(request, 'You have been Logged In')
            return redirect('website:home')
        else:
            messages.success(request, 'There was an Error, Please try again!')
            return redirect('website:home')
    else:
        return render(request, 'website/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass