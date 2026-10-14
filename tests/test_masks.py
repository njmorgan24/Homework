import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("card_number", "expected"),
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Проверяет маскирование номеров карт в формате XXXX XX** **** XXXX."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", ["", "   ", "1234"])
def test_get_mask_card_number_missing_or_short(card_number: str) -> None:
    """Проверяет устойчивость функции к отсутствию и неполной длине номера."""
    assert isinstance(get_mask_card_number(card_number), str)


@pytest.mark.parametrize(
    ("account_number", "expected"),
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("4305", "**4305"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Проверяет маскирование номеров счетов в формате **XXXX."""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    ("account_number", "expected"),
    [
        ("123", "**123"),
        ("1", "**1"),
        ("", "**"),
    ],
)
def test_get_mask_account_shorter_than_expected(
    account_number: str, expected: str
) -> None:
    """Проверяет работу функции с номером счёта короче ожидаемой длины."""
    assert get_mask_account(account_number) == expected
