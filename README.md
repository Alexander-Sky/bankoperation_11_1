# Банковский виджет операций

## Описание проекта
Проект представляет собой набор инструментов для обработки банковских операций. Основные функции включают фильтрацию и сортировку операций по различным критериям.

## Установка

### Требования
* Python 3.14+
* Poetry для управления зависимостями

### Установка проекта
```bash
# Клонирование репозитория
git clone https://github.com/Alexander-Sky/bankoperation_11_1.git

# Установка зависимостей через Poetry
poetry install
poetry shell

## Зависимости

### Основные зависимости
- pytest - фреймворк для тестирования
- pytest-cov - плагин для измерения покрытия
- coverage - инструмент для анализа покрытия

### Инструменты разработки
- flake8 - проверка стиля кода
- black . - форматирование кода
- isort . - сортировка импортов
- mypy src- статическая типизация

## Запуск тестов
```bash

# Запуск всех тестов
pytest

# Запуск с измерением покрытия
pytest --cov=src --cov-report=html

## Использование
### Импорт функций
python

from src.processing import filter_by_state, sort_by_date

from generators.generators import card_number_generator

## Примеры работы
### Пример фильтрации операций
python

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по умолчанию (EXECUTED)
filtered_operations = filter_by_state(operations)

# Фильтрация по CANCELED
cancelled_operations = filter_by_state(operations, 'CANCELED')

### Реализация функций

Основные функции обработки

from typing import List, Dict

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрация операций по состоянию"""
    return [op for op in operations if op.get('state') == state]

def sort_by_date(operations: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортировка операций по дате"""
    return sorted(operations, key=lambda x: x['date'], reverse=descending)

## Функций с использованием генераторов

def card_number_generator(start: int, stop: int):
    """Генератор номеров карт"""
    for number in range(start, stop + 1):
        formatted = f"{number:016d}"
        yield f"{formatted[:4]} {formatted[4:8]} {formatted[8:12]} {formatted[12:]}"


## Тестирование

Текущее покрытие: 98%
Цель: 100% покрытие тестами

### Запуск тестов с покрытием

# Генерация HTML-отчета
pytest --cov=src --cov-report=html

# Просмотр отчета
open htmlcov/index.html

## Генерация отчета о покрытии

После выполнения команды выше:

    В папке htmlcov появится отчет

    Откройте файл htmlcov/index.html для просмотра отчета

### Требования к тестированию

    Покрытие кода тестами не менее 80%

    Все критические ветки кода должны быть протестированы

    Проверка корректности работы всех функций

## Документация

### Основные модули:

    masks.py - функции маскирования номеров карт и счетов

    widget.py - функции форматирования данных для отображения

    processing.py - функции обработки операций

    conftest.py - фикстуры для тестирования
    

## Вклад в проект

### Для внесения изменений:

    Создайте новую ветку от develop

    Внесите изменения

    Создайте Pull Request

    Дождитесь ревью