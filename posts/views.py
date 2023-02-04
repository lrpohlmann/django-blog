from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "paginas/home.html")


def post_view(request):
    return render(request, "paginas/post.html")
