from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Проверяет маскировку номера карты из 16 цифр."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_length() -> None:
    """Проверяет, что результат сохраняет исходную длину номера."""
    assert len(get_mask_card_number("7000792289606361")) == len("7000 79** **** 6361")


def test_get_mask_account() -> None:
    """Проверяет маскировку длинного номера счёта."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_min_length() -> None:
    """Проверяет маскировку номера счёта минимальной длины (4 символа)."""
    assert get_mask_account("4305") == "**4305"
