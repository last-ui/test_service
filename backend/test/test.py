import asyncio
import json
import os
from datetime import datetime
from random import sample

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from exceptions import EmptyDBException
from jservice import get_questions_from_api

from api.v1.serializers import QuestionSerializer
from question.models import Category, Question


class Test:
    """Тестовый класс сервиса."""

    def __init__(self, question_count: int = 1, result_count: int = 1):
        """Конструктор класса Test."""
        self.quiz_count: int = self._is_valid_type(
            question_count, "question_count"
        )
        self.result_count: int = self._is_valid_type(
            result_count, "result_count"
        )

    def create_new_questions(self) -> None:
        """Метод создания в БД, полученных с внешнего API вопросов викторин."""
        db_questions = Question.objects.values_list(
            "question_id", flat=True
        ).all()
        api_questions = asyncio.run(self._get_questions(set(db_questions)))
        self._create_db_questions(api_questions)

    @staticmethod
    def get_category_question_count(category: str) -> int:
        """Метод получения кол-ва вопросов в заданной категории."""
        category = Category.objects.filter(title=category).first()
        if category:
            return category.questions.count()
        return 0

    def get_db_questions(self) -> None:
        """Получение вопросов из БД."""
        questions = Question.objects.all()
        if not questions:
            raise EmptyDBException("Empty DataBase")
        if len(questions) <= self.result_count:
            count = len(questions)
        else:
            count = self.result_count
        questions = sample(list(questions), count)

        serializer = QuestionSerializer(questions, many=True)

        self._save_json(serializer.data)

    def _read_json(self, filename: str) -> list | None:
        """Чтение дампа данных из json-файла."""
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as data:
                json_data = json.load(data)
                if not json_data:
                    return None
                return json_data
        except FileNotFoundError:
            return None

    def _save_json(self, data: list) -> None:
        """Запись данных в json-файл."""
        if not data:
            return
        date = datetime.now().date().isoformat()

        json_data = self._read_json(date)
        if not json_data:
            json_data = []
        json_data.extend(data)
        with open(f"{date}.json", "w", encoding="utf-8") as output_data:
            json.dump(data, output_data)

    def _create_db_questions(self, api_questions: dict) -> None:
        """Создание вопросов с категориями в БД."""
        questions = []
        for question in api_questions:
            api_category = question.get("category")
            category, _ = Category.objects.get_or_create(
                title=api_category["title"]
            )
            questions.append(
                Question(
                    question_id=question.get("id"),
                    question_text=question.get("question"),
                    answer_text=question.get("answer"),
                    category=category,
                ),
            )
        Question.objects.bulk_create(questions)

    async def _get_questions(self, db_questions: set) -> dict:
        """Асинхронный метод получения вопросов с внешнего API."""
        questions_from_api = await get_questions_from_api(
            self.quiz_count, db_questions
        )
        return questions_from_api

    @staticmethod
    def _is_valid_type(param: int, param_name: str) -> int:
        """Метод валидации входных аргументов."""
        if not isinstance(param, int):
            raise TypeError(f"Parameter '{param_name}' is not integer")
        if param < 1:
            raise ValueError(f"Parameter '{param_name}' must be positive")
        return param


if __name__ == "__main__":
    test = Test(question_count=2, result_count=4)
    test.get_db_questions()
    test.create_new_questions()
    print(test.get_category_question_count(category="trauma"))
