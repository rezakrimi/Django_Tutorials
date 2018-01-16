from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    re_path(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html"))
]
