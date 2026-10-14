from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Маскирует номер карты или счёта, сохраняя его тип.

    Принимает одну строку вида ``Visa Platinum 7000792289606361`` или
    ``Счет 73654108430135874305`` и возвращает её с замаскированным
    номером. Для маскировки переиспользуются функции из модуля
    :mod:`src.masks`.

    Строка не разбивается на отдельные аргументы: тип и номер передаются
    вместе. Последнее слово считается номером, всё, что стоит перед ним,
    — названием карты или счёта (название может состоять из нескольких слов).

    :param account_card: Строка с типом и номером карты или счёта.
    :return: Строка с замаскированным номером.
    :raises ValueError: Если ввод пустой или не содержит номер.
    """
    parts = account_card.split()
    if len(parts) < 2:
        raise ValueError(
            "Некорректный ввод: ожидается тип и номер, разделённые пробелом"
        )

    *name_parts, number = parts
    name = " ".join(name_parts)

    if "счет" in name.lower() or "счёт" in name.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO-формата в формат ``ДД.ММ.ГГГГ``.

    :param date_string: Дата в ISO-формате, например
        ``2024-03-11T02:26:18.671407``.
    :return: Дата в формате ``11.03.2024``.
    """
    return datetime.fromisoformat(date_string).strftime("%d.%m.%Y")
