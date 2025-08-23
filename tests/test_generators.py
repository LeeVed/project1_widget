import re

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions

transactions = [
    {"id": 1, "operationAmount": {"amount": "150", "currency": {"code": "USD"}}},
    {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}},
    {"id": 3, "operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
]


def test_filter_by_currency() -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in result)


def test_filter_by_currency_no_usd(transactions_no_usd: list) -> None:
    result = list(filter_by_currency(transactions_no_usd, "USD"))
    assert len(result) == 0


def test_filter_by_currency_empty_list(transactions_empty_list: list) -> None:
    result = list(filter_by_currency(transactions_empty_list, "USD"))
    assert len(result) == 0


def test_transaction_descriptions(transactions_data: list) -> None:
    descriptions = transaction_descriptions(transactions_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод с карты на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на карту"
    assert next(descriptions) == "Перевод с карты на карту"


def test_card_number_generator() -> None:
    start, stop = 4000123456788000, 4000123456788002
    expected_cards = ["4000 1234 5678 8000", "4000 1234 5678 8001", "4000 1234 5678 8002"]
    generated_cards = [card for card in card_number_generator(start, stop)]
    assert generated_cards == expected_cards


def test_card_number_formatting() -> None:
    start, stop = 4000123456788000, 4000123456788002
    card_format_pattern = re.compile(r"^\d{4} \d{4} \d{4} \d{4}$")
    for card in card_number_generator(start, stop):
        assert card_format_pattern.match(card), f"Номер карты {card} не соответствует формату"


def test_card_number_generator_boundary() -> None:
    start, stop = 4000123456788000, 4000123456788002
    expected_cards = ["4000 1234 5678 8000", "4000 1234 5678 8001", "4000 1234 5678 8002"]
    generated_cards = [card for card in card_number_generator(start, stop)]
    assert generated_cards == expected_cards, "Генератор не выдаёт все значения в диапазоне, включая крайние"
