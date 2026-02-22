import pytest
from generators.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)

@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        # Добавьте другие тестовые транзакции здесь
    ]

def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    # Проверяем, что хотя бы одна транзакция найдена
    assert len(list(usd_transactions)) >= 1

def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    expected = [transaction['description'] for transaction in transactions]
    assert list(descriptions) == expected

@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005"
            ]
        )
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
