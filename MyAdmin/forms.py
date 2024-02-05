from django import forms
from .models import User
from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='User Id')
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    jobPosition = forms.CharField(max_length=100, label='Job Title')
