import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "entry_value, expected",
    [
    ("блда бла 1234567891123456", "блда бла 1234 56** **** 3456"),
    ("блда бла 123456789112345s", "Некорректный номер карты"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 64686473678894779000", "Счет **9000"),
    ("Счет 6468647367889477958X", "Некорректный номер счета"),
    ("Счет 73678894779589", "Некорректный номер счета"),
    ])

def test_mask_account_card(entry_value, expected):
    assert mask_account_card(entry_value) == expected