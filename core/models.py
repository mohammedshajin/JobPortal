from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.forms.fields import ImageField
from django.urls import reverse

EXPERIENCE_CHOICES = [
    ("0-1", "0-1"),
    ("1-2", "1-2"),
    ("2-3", "2-3"),
    ("3-4", "3-4"),
    ("5-10", "5-10"),
]

JOBTYPE_CHOICES = [
    ("Full-time", "Full-time"),
    ("Part-time", "Part-time"),
    ("Freelance", "Freelance"),
    ("Internship", "Internship"),
    ("Permanent", "Permanent"),
    ("Contract", "Contract"),
]

choices = [('0-100000', '0-100000'), ('100000-200000', '100000-200000'), ('200000-300000', '200000-300000'), ('400000-500000', '400000-500000'), ('500000-1000000', '500000-1000000'), ('Negotiable', 'Negotiable')]



class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField(upload_to='assets', blank=True, null=True, default="static/images/bi.jpg")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    location = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255)
    posted = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100, choices=choices, default='0-100000')
    experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES, default='0-1')
    jobtype = models.CharField(max_length=100, choices=JOBTYPE_CHOICES, default='Full-time')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_single',args=[self.slug])
