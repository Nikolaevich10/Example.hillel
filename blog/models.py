from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    DRAFT = "draft"
    PUBLISHED = "published"
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[
                             self.slug])

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title