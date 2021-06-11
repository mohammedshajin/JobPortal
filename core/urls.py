from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', auth_view.LogoutView.as_view(), name ='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name ='login'),
    path('post-job/', views.post_job, name="post_job"),
    path('job-list/', views.job_list, name="job_list"),
]
