from django.db import models


class Category(models.Model):
    title = models.CharField(
        "Заголовок категории", max_length=256, unique=True
    )


class Question(models.Model):
    """Модель вопросов викторины."""

    question_id = models.PositiveIntegerField(
        "ID вопроса", unique=True, null=False, blank=False
    )

    question_text = models.TextField(
        "Текст вопроса",
        null=False,
        blank=False,
        max_length=256,
    )

    answer_text = models.TextField(
        "Текст ответа",
        null=False,
        blank=False,
        max_length=256,
    )

    category = models.ForeignKey(
        Category,
        verbose_name="Категория вопроса",
        on_delete=models.CASCADE,
        related_name="questions",
    )
