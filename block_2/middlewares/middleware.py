import json

from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)

import sys


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """
    pass


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """
    pass


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """
    pass



