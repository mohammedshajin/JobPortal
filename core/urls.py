from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('logout/', auth_view.LogoutView.as_view(), name ='logout'),
    path('post-job/', views.post_job, name="post_job"),
    path('job-list/', views.job_list, name="job_list"),
    path('search/', views.search, name='search'),
    path('<slug:job>/', views.job_single, name='job_single'),
]
