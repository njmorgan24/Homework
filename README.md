# bank-widget

Виджет для личного кабинета клиента банка. Проект готовит данные о последних
успешных банковских операциях для отображения в новом виджете.

## Структура проекта

```
.
├── src/                # исходный код
│   ├── __init__.py
│   ├── masks.py        # функции маскировки карты и счёта
│   └── widget.py       # mask_account_card и get_date
├── tests/              # тесты
│   ├── __init__.py
│   ├── test_masks.py
│   └── test_widget.py
├── .flake8             # конфигурация Flake8
├── pyproject.toml      # зависимости и настройки black, isort, mypy
└── README.md
```

## Установка

```bash
poetry install --with lint,dev
```

## Функции модуля `src.masks`

- `get_mask_card_number(card_number)` — маскирует номер карты в формате
  `XXXX XX** **** XXXX`.

  ```python
  >>> from src.masks import get_mask_card_number
  >>> get_mask_card_number("7000792289606361")
  '7000 79** **** 6361'
  ```

- `get_mask_account(account_number)` — маскирует номер счёта в формате `**XXXX`.

  ```python
  >>> from src.masks import get_mask_account
  >>> get_mask_account("73654108430135874305")
  '**4305'
  ```

## Функции модуля `src.widget`

- `mask_account_card(account_card)` — принимает одну строку с типом и номером
  карты или счёта и возвращает её с замаскированным номером. Последнее слово
  считается номером, остальное — названием (может состоять из нескольких слов).
  Бросает `ValueError` при пустом вводе или отсутствии номера.

  ```python
  >>> from src.widget import mask_account_card
  >>> mask_account_card("Visa Platinum 7000792289606361")
  'Visa Platinum 7000 79** **** 6361'
  >>> mask_account_card("Счет 73654108430135874305")
  'Счет **4305'
  ```

- `get_date(date_string)` — преобразует дату из ISO-формата в формат
  `ДД.ММ.ГГГГ`.

  ```python
  >>> from src.widget import get_date
  >>> get_date("2024-03-11T02:26:18.671407")
  '11.03.2024'
  ```

## Проверка качества кода

```bash
poetry run flake8 src tests
poetry run black --check src tests
poetry run isort --check-only src tests
poetry run mypy src
```

## Тесты

```bash
poetry run pytest
```
