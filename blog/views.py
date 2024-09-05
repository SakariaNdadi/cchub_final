from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)
from .models import Post

# def index(request):
#     return render(request, "blog/list.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
