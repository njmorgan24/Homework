# bank-widget

## Цель проекта

Виджет для личного кабинета клиента банка. Проект готовит данные о последних
успешных банковских операциях для отображения в новом виджете: маскирует номера
карт и счетов, форматирует даты, а также фильтрует и сортирует список операций
по статусу и дате.

## Структура проекта

```
.
├── src/                # исходный код
│   ├── __init__.py
│   ├── masks.py        # функции маскировки карты и счёта
│   ├── widget.py       # mask_account_card и get_date
│   └── processing.py   # filter_by_state и sort_by_date
├── tests/              # тесты
│   ├── __init__.py
│   ├── test_masks.py
│   ├── test_widget.py
│   └── test_processing.py
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

## Функции модуля `src.processing`

- `filter_by_state(transactions, state="EXECUTED")` — возвращает новый список
  операций, у которых ключ `state` равен указанному значению.

  ```python
  >>> from src.processing import filter_by_state, sort_by_date
  >>> operations = [
  ...     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  ...     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
  ...     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
  ...     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
  ... ]
  >>> filter_by_state(operations)
  [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
  >>> filter_by_state(operations, "CANCELED")
  [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
  ```

- `sort_by_date(transactions, reverse=True)` — возвращает новый список
  операций, отсортированный по дате. По умолчанию — по убыванию (сначала самые
  последние операции).

  ```python
  >>> sort_by_date(operations)
  [{'id': 41428829, ...}, {'id': 615064591, ...}, {'id': 594226727, ...}, {'id': 939719570, ...}]
  >>> sort_by_date(operations, reverse=False)
  [{'id': 939719570, ...}, {'id': 594226727, ...}, {'id': 615064591, ...}, {'id': 41428829, ...}]
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
