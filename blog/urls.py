from django.conf.urls import url
from . import views

from django.urls import path

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
]
