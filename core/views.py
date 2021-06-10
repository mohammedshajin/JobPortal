from django.shortcuts import render
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login 
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'index.html', {'form': form})
from django.contrib.auth import authenticate, login


