from django.db import models


class Picture(models.Model):
    description = models.TextField(
        "Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        "Изображение",
        upload_to="media/",
    )
