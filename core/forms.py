from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import json
from.models import Job
from django.forms import ModelForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )

class UploadForm(ModelForm):
    class Meta:
        model = Job
        fields = ("image", "title", "desc", "location", "salary", "experience", "jobtype")

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']        
