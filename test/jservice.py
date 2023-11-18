import asyncio

import aiohttp
import exceptions as ex

PUBLIC_API_URL: str = "https://jservice.io/api/"


async def get_questions_from_url(session, url, db_questions):
    while True:
        try:
            async with session.get(url) as response:
                questions = await response.json()
        except Exception as error:
            raise ex.UnknownAPIException(
                f"public API return incorrect result: {error}",
            )
        if not isinstance(questions, list):
            raise ex.APIResponseTypeErrorException(
                "public API return incorrect result",
            )
        if not isinstance(questions[0], dict):
            raise ex.APIResponseTypeErrorException(
                "public API return incorrect result",
            )
        if not db_questions:
            return questions[0]
        if questions[0]["id"] not in db_questions:
            return questions[0]


async def get_questions_from_api(count, db_questions):
    async with aiohttp.ClientSession() as session:
        task = []
        for number in range(1, count + 1):
            question_url = f"{PUBLIC_API_URL}random"
            task.append(
                asyncio.ensure_future(
                    get_questions_from_url(session, question_url, db_questions)
                )
            )
        api_questions = await asyncio.gather(*task)
    return api_questions
