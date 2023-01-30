from typing import Iterable, Optional
import uuid
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False, unique=True)
    data_criacao = models.DateField("data de criação", auto_now_add=True)
    autor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    corpo = models.TextField(max_length=2000, null=False, blank=False)
    assuntos = models.ManyToManyField("Assunto", null=False, blank=False)
    slug = models.SlugField(null=True)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None:
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(force_insert, force_update, using, update_fields)


class Assunto(models.Model):
    nome = models.CharField(max_length=15, null=False, blank=False, unique=True)
