from django.core import paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import RegisterForm, UploadForm, LoginForm
from django.contrib.auth import login 
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Job
from django.core.paginator import Paginator, EmptyPage
from .filters import JobFilter
from django.db.models import Q
from blog.models import Post

def home(request):
    form = LoginForm()
    rform = RegisterForm()
    
    if request.method == "POST" and 'Register' in request.POST:
            rform = RegisterForm(request.POST)
            if rform.is_valid():
                user = rform.save()
                login(request, user)
            else:
                rform = RegisterForm()
            return redirect('home')

    elif request.method == "POST" and 'Login' in request.POST:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
            else:
                form = LoginForm()
            return redirect('home')
    
    all_posts = Post.objects.all()

    return render(request, 'index.html', {'rform': rform, 'form':form, 'all_posts':all_posts})


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
    myFilter = JobFilter(request.GET, queryset=jobs)
    jobs = myFilter.qs
    paginator = Paginator(jobs, 6)
    page = request.GET.get('page')
    jobs = paginator.get_page(page)

    

    return render(request, 'job_list.html', {'jobs':jobs, 'myFilter': myFilter})

def job_single(request, job):
    all_jobs = Job.objects.all()

    job = get_object_or_404(Job, slug=job)

    return render(request, 'job_single.html', {'job' : job, 'all_jobs':all_jobs})

def search(request):
    query = request.GET.get('query', '')
    jobs = Job.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))

    return render(request, 'search.html', {'jobs': jobs, 'query': query})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')