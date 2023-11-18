from django.db import models


class Picture(models.Model):
    """Модель Picture."""

    description = models.TextField(
        "Описание",
        blank=False,
        null=False,
    )
    image = models.ImageField(
        "Изображение",
        upload_to="media/",
    )
