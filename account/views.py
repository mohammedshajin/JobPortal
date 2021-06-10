from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login 

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
            
    


# Create your views here.
