# bank-widget

Виджет для личного кабинета клиента банка. Проект готовит данные о последних
успешных банковских операциях для отображения в новом виджете.

## Структура проекта

```
.
├── src/                # исходный код
│   ├── __init__.py
│   └── masks.py        # функции маскировки карты и счёта
├── tests/              # тесты
│   ├── __init__.py
│   └── test_masks.py
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
