class BadRequest(Exception):
    """Ошибка доступа к эндпоинту."""


class APIResponseTypeErrorException(TypeError):
    """Ошибка типа данных в ответе API."""


class UnknownAPIException(Exception):
    """Ошибка при отправке запроса к API."""


class EmptyDBException(Exception):
    """В базе данных отсутствуют записи."""
