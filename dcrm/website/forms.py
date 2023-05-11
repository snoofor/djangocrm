# In order to get username, email, password for new user we will use forms.py
# User Creation Forms of Django will be used but, for signature form we will not use {{forms}}
# SignUpForm and Class check - flatplanet/Django-CRM/website/forms.py github repository

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from .models import Record
import logging
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from django.conf import settings

logger = logging.getLogger(__name__)

text_valid_domains = staticfiles_storage.path(r'website/validdomains.txt')

with open(os.path.join(settings.STATIC_ROOT, f'{text_valid_domains}'), 'r', encoding='utf8') as d:
     text_read = d.readlines()

VALID_DOMAINS = text_read[1]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(error_messages={"required": "Please enter email"}, 
                             label='', 
                             max_length=50, 
                             min_length=13,
                             widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':f'Email min 13 characters, {VALID_DOMAINS} domains only'}))
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

    def clean_email(self, *args, **kwargs):
        original_email = self.cleaned_data['email']
        domain = self.cleaned_data["email"].split("@")[-1]
        if domain not in VALID_DOMAINS:
            raise ValidationError("E-mail addresses from %(domain)s are not allowed.", code="invalid", params={"domain": domain})
        return original_email

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small></small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password must contain at least 8 characters.</small></span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Please, enter the same password as before.</small></span>'



# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)

    