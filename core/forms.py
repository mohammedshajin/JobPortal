from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import json
from.models import Job
from django.forms import ModelForm

choices = [('0-100000', '0-100000'), ('100000-200000', '100000-200000'), ('200000-300000', '200000-300000'), ('400000-500000', '400000-500000'), ('500000-1000000', '500000-1000000'), ('Negotiable', 'Negotiable')]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )

class UploadForm(ModelForm):
    class Meta:
        model = Job
        fields = ("image", "title", "desc", "location", "salary", "experience" )

        widgets = {
            'salary':forms.Select(choices=choices, attrs={'class': 'form-control'})
        }
