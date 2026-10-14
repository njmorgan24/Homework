from src.processing import filter_by_state, sort_by_date

TRANSACTIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_default() -> None:
    """Проверяет фильтрацию по статусу 'EXECUTED' по умолчанию."""
    assert filter_by_state(TRANSACTIONS) == [TRANSACTIONS[0], TRANSACTIONS[1]]


def test_filter_by_state_canceled() -> None:
    """Проверяет фильтрацию по явно переданному статусу 'CANCELED'."""
    assert filter_by_state(TRANSACTIONS, "CANCELED") == [
        TRANSACTIONS[2],
        TRANSACTIONS[3],
    ]


def test_filter_by_state_does_not_mutate_source() -> None:
    """Проверяет, что исходный список не изменяется."""
    original = [transaction.copy() for transaction in TRANSACTIONS]
    filter_by_state(TRANSACTIONS, "CANCELED")
    assert TRANSACTIONS == original


def test_sort_by_date_descending() -> None:
    """Проверяет сортировку по убыванию даты (по умолчанию)."""
    assert sort_by_date(TRANSACTIONS) == [
        TRANSACTIONS[0],
        TRANSACTIONS[3],
        TRANSACTIONS[2],
        TRANSACTIONS[1],
    ]


def test_sort_by_date_ascending() -> None:
    """Проверяет сортировку по возрастанию даты."""
    assert sort_by_date(TRANSACTIONS, reverse=False) == [
        TRANSACTIONS[1],
        TRANSACTIONS[2],
        TRANSACTIONS[3],
        TRANSACTIONS[0],
    ]
