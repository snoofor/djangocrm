from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required # if not login do not show the page
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.

@login_required(login_url="/accounts/login/") # login_requierd, if not login redirect to login page
def home(request):
    return render(request, 'website/home.html', {})

# Creation of user Model class based view
# class SignUpView(CreateView): # inherited from CreateView
#    form_class = UserCreationForm
#    # success_url = reverse("login") reverse will work each time, instead use reverse_lazy
#    success_url = reverse_lazy("login") # reverse_lazy will work if reached
#    template_name = "registration/signup.html"

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout")
    return redirect("home")

def signup_user(request):
    return render(request, 'registration/signup.html', {})