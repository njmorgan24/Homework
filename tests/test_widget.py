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
    """Проверяет распознавание карты/счёта и корректную маскировку номера."""
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize("account_card", ["", "   ", "Maestro", "Счет", "Visa"])
def test_mask_account_card_invalid_input(account_card: str) -> None:
    """Проверяет устойчивость функции к некорректному вводу."""
    with pytest.raises(ValueError):
        mask_account_card(account_card)


@pytest.mark.parametrize(
    ("date_string", "expected"),
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30", "30.06.2018"),
        ("2018-06-30T02:08:58", "30.06.2018"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    """Проверяет преобразование корректных дат из ISO-формата."""
    assert get_date(date_string) == expected


@pytest.mark.parametrize("date_string", ["", "not-a-date", "2024-13-40T00:00:00"])
def test_get_date_invalid_input(date_string: str) -> None:
    """Проверяет, что при некорректной дате возникает ValueError."""
    with pytest.raises(ValueError):
        get_date(date_string)
