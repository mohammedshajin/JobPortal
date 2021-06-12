from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', auth_view.LogoutView.as_view(), name ='logout'),
    path('post-job/', views.post_job, name="post_job"),
    path('job-list/', views.job_list, name="job_list"),
]
