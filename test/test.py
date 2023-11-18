import asyncio

from jservice import get_questions_from_api


class Test:
    def __init__(self, quiz_count: int = 1, result_count: int = 1):
        self.quiz_count: int = self._is_valid_type(quiz_count, "quiz_count")
        self.result_count: int = self._is_valid_type(
            result_count, "result_count"
        )

    def get_quiz(self):
        return asyncio.run(self._get_quiz())

    def _get_db_questions(self):
        pass

    async def _get_quiz(self):
        questions_from_api = await get_questions_from_api(self.quiz_count, [])
        return questions_from_api

    @staticmethod
    def _is_valid_type(param, param_name):
        if not isinstance(param, int):
            raise TypeError(f"Parameter '{param_name}' is not integer")
        return param


test = Test(quiz_count=1, result_count=1)
test.get_quiz()
