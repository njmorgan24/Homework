from typing import Any

import pytest


@pytest.fixture
def transactions() -> list[dict[str, Any]]:
    """Основной набор операций с разными статусами и датами."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_without_executed() -> list[dict[str, Any]]:
    """Набор операций, в котором нет статуса EXECUTED."""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_same_date() -> list[dict[str, Any]]:
    """Набор операций с одинаковыми датами для проверки стабильности сортировки."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T10:00:00.000000"},
    ]


@pytest.fixture
def empty_transactions() -> list[dict[str, Any]]:
    """Пустой список операций."""
    return []
