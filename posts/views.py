from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest

from .models import Post

# Create your views here.
def home_view(request: HttpRequest):
    return render(request, "paginas/home.html")


def post_view(request: HttpRequest, pk: int):
    return render(
        request, "paginas/post.html", {"post": get_object_or_404(Post, pk=pk)}
    )


def posts_grid_view(request: HttpRequest):
    return render(request, "partials/grid-posts.html", {"posts": Post.objects.all()})
