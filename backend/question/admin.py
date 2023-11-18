from django.contrib import admin

from question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Управление вопросами викторины."""

    list_display = ("question_id", "question_text")
    search_fields = ("question_text",)
