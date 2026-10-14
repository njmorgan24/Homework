import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("account_card", "expected"),
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    """Проверяет маскировку карт и счетов с сохранением их типа."""
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize("account_card", ["", "   ", "Maestro"])
def test_mask_account_card_invalid_input(account_card: str) -> None:
    """Проверяет защиту от некорректного ввода: пустая строка или нет номера."""
    with pytest.raises(ValueError):
        mask_account_card(account_card)


def test_get_date() -> None:
    """Проверяет преобразование даты из ISO-формата в ДД.ММ.ГГГГ."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
