# Generated by Django 4.1.5 on 2023-01-30 01:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
