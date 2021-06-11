from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.forms.fields import ImageField

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField(upload_to='assets', blank=True, null=True, default="static/images/bi.jpg")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    location = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255)
    posted = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100)
    experience = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title
