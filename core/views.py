from django.shortcuts import render
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import RegisterForm, UploadForm
from django.contrib.auth import login 
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Job

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


@login_required
def post_job(request):
    if request.method == "POST":
        form = UploadForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.slug = slugify(job.title)
            job.save()
        return redirect('job_list')
    else:
        form = UploadForm()
    return render(request, 'post_job.html', {'form':form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs':jobs})