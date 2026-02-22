def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте

    :param transactions: список словарей с транзакциями
    :param currency: код валюты для фильтрации
    :return: итератор с отфильтрованными транзакциями
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction