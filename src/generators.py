from typing import Generator
from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    counter = 0
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            counter += 1
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты
    и в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for card in range(start, stop + 1):
        card_str = str(card).zfill(16)
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted_card
