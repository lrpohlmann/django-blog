from django.urls import path

from .views import post_view, home_view


app_name = "posts"

urlpatterns = [
    path("", home_view, name="home_view"),
    path("post/<int:pk>", post_view, name="post_view"),
]
