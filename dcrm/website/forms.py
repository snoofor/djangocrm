# In order to get username, email, password for new user we will use forms.py
# User Creation Forms of Django will be used but, for signature form we will not use {{forms}}
# SignUpForm and Class check - flatplanet/Django-CRM/website/forms.py github repository

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(error_messages={"required": "Please enter email"}, 
                             label='', 
                             max_length=50, 
                             min_length=13,
                             widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email between min 13 characters'}))
    first_name = forms.CharField(error_messages={"required": "Please enter your name"}, 
                                 label='', 
                                 max_length=18, 
                                 min_length=3,
                                 widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name between 3 and 18 characters'}))
    last_name = forms.CharField(error_messages={"required": "Please enter your last name"}, 
                                label='', 
                                max_length=18, 
                                min_length=2,
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name between 2 and 18 characters'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must contain at least 8 characters.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Please, enter the same password as before.</small></span>'

    