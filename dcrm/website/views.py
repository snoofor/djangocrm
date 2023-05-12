from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm, AddRecordForm, RecordNameFilterForm
from .models import Record
from .filters import RecordFilter

# Create your views here.

#@login_required(login_url="/accounts/login/") # login_requierd, if not login redirect to login page
"""def home(request):
    records = Record.objects.all()
    return render(request, 'website/home.html', {'records':records})"""

@login_required(login_url="/accounts/login/") # login_requierd, if not login redirect to login page
def home(request):
    record_filter = RecordFilter(request.GET, queryset=Record.objects.all())
    context = {
        'form' : record_filter.form,
        'records' : record_filter.qs
    }
    return render(request, 'website/home.html', context)

# Creation of user Model class based view
# class SignUpView(CreateView): # inherited from CreateView
#    form_class = UserCreationForm
#    # success_url = reverse("login") reverse will work each time, instead use reverse_lazy
#    success_url = reverse_lazy("login") # reverse_lazy will work if reached
#    template_name = "registration/signup.html"

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout")
    return redirect("login")

def signup_user(request):

    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, f'You have been succesfully Registered. Welcome {user.username}')
            return redirect("website:home")
    else:
        form = SignUpForm()
        # return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
            # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('website:home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, f'You have deleted the customer with id: {pk}')
        return redirect("website:home")
    else:
        messages.success(request, f'You must be logged in!')
        return redirect("website:home")
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.POST:
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added.')
                return redirect('website:home')
        return render(request, 'website/add_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in!')
        return redirect("website:home")
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been updated.')
            return redirect("website:home")
        return render(request, 'website/update_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in!')
        return redirect("website:home")
    
    
# RecordNameFilterForm is at forms.py - RecordFilter is at filters.py

def records_filter(request):
    first_name = request.GET.get('first_name')
    records = Record.objects.all()
    if first_name:
        records = records.filter(first_name__icontains=first_name)
    context = {
        'form' : RecordNameFilterForm(),
        'records' : records
    }
    return render(request, 'website:home', context)