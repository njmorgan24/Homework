from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    ("state", "expected_ids"),
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(
    transactions: list[dict[str, Any]], state: str, expected_ids: list[int]
) -> None:
    """Проверяет фильтрацию по разным значениям статуса."""
    result = filter_by_state(transactions, state)
    assert [transaction["id"] for transaction in result] == expected_ids


def test_filter_by_state_default_is_executed(
    transactions: list[dict[str, Any]],
) -> None:
    """Проверяет, что по умолчанию фильтрация идёт по статусу EXECUTED."""
    result = filter_by_state(transactions)
    assert all(transaction["state"] == "EXECUTED" for transaction in result)
    assert len(result) == 2


def test_filter_by_state_empty_result(
    transactions_without_executed: list[dict[str, Any]],
) -> None:
    """Проверяет возврат пустого списка, если нужного статуса нет."""
    assert filter_by_state(transactions_without_executed) == []


def test_filter_by_state_does_not_mutate_source(
    transactions: list[dict[str, Any]],
) -> None:
    """Проверяет, что исходный список не изменяется."""
    original = [transaction.copy() for transaction in transactions]
    filter_by_state(transactions, "CANCELED")
    assert transactions == original


def test_sort_by_date_default_descending(
    transactions: list[dict[str, Any]],
) -> None:
    """Проверяет сортировку по убыванию даты по умолчанию."""
    result = sort_by_date(transactions)
    assert [transaction["id"] for transaction in result] == [
        41428829,
        615064591,
        594226727,
        939719570,
    ]


def test_sort_by_date_ascending(
    transactions: list[dict[str, Any]],
) -> None:
    """Проверяет сортировку по возрастанию даты."""
    result = sort_by_date(transactions, reverse=False)
    assert [transaction["id"] for transaction in result] == [
        939719570,
        594226727,
        615064591,
        41428829,
    ]


def test_sort_by_date_equal_dates_keeps_order(
    transactions_same_date: list[dict[str, Any]],
) -> None:
    """Проверяет, что при одинаковых датах сохраняется исходный порядок."""
    result = sort_by_date(transactions_same_date)
    assert [transaction["id"] for transaction in result] == [1, 2]


def test_sort_by_date_does_not_mutate_source(
    transactions: list[dict[str, Any]],
) -> None:
    """Проверяет, что исходный список не изменяется."""
    original = [transaction.copy() for transaction in transactions]
    sort_by_date(transactions)
    assert transactions == original


def test_sort_by_date_empty(empty_transactions: list[dict[str, Any]]) -> None:
    """Проверяет сортировку пустого списка."""
    assert sort_by_date(empty_transactions) == []
