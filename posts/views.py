from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def home_view(request):
    return render(request, "paginas/home.html")


def post_view(request, pk: int):
    return render(
        request, "paginas/post.html", {"post": get_object_or_404(Post, pk=pk)}
    )
