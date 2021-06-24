from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name="blog"),
        path('<slug:post>/', views.post_single, name='post_single'),
    ]