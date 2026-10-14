from typing import Any


def filter_by_state(
    transactions: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Фильтрует список банковских операций по значению ключа ``state``.

    Возвращает новый список, содержащий только те словари, у которых ключ
    ``state`` равен переданному значению. Исходный список не изменяется.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Значение ключа ``state`` для фильтрации
        (по умолчанию ``'EXECUTED'``).
    :return: Новый отфильтрованный список словарей.
    """
    return [
        transaction for transaction in transactions if transaction.get("state") == state
    ]


def sort_by_date(
    transactions: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует список банковских операций по дате.

    Возвращает новый список, отсортированный по ключу ``date``. Исходный
    список не изменяется. Даты в ISO-формате сравниваются как строки, что
    соответствует хронологическому порядку.

    :param transactions: Список словарей с данными о банковских операциях.
    :param reverse: Порядок сортировки. По умолчанию ``True`` — по убыванию
        (сначала самые последние операции).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        transactions, key=lambda transaction: transaction["date"], reverse=reverse
    )
