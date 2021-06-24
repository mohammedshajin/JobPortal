from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post (models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(verbose_name='Add thumbnail', blank=True, upload_to='thumbnails')
    image = models.ImageField(verbose_name='Add image', blank=True, upload_to='images')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title