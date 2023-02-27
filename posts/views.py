from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from django.core.paginator import Paginator, EmptyPage, Page

from .models import Post

# Create your views here.
def home_view(request: HttpRequest):
    return render(request, "paginas/home.html")


def post_view(request: HttpRequest, pk: int):
    return render(
        request, "paginas/post.html", {"post": get_object_or_404(Post, pk=pk)}
    )


def posts_grid_view(request: HttpRequest):
    pagina_posts = Paginator(Post.objects.all().order_by("-data_criacao"), 9).get_page(
        request.GET.get("pagina")
    )
    return render(
        request,
        "partials/grid-posts.html",
        {"posts": pagina_posts.object_list, "pagina_obj": pagina_posts},
    )
