from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status=Post.PUBLISHED)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,
                                   status='published',
                                   )
    return render(request, 'blog/post/ detail.html', {'post': post})