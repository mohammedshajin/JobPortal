from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
    all_posts = Post.objects.all()
    return render(request, 'blog.html', {'all_posts':all_posts})

def post_single(request, post):
    all_posts = Post.objects.all()

    post = get_object_or_404(Post, slug=post)

    return render(request, 'post.html', {'post' : post, 'all_posts':all_posts})