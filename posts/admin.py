from django.contrib import admin

from posts.models import Post, Assunto

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    fields = ("titulo", "autor", "corpo", "assuntos")


@admin.register(Assunto)
class AssuntoModel(admin.ModelAdmin):
    pass
