import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize("card_number, expected", [("1234567890123456", "1234 56** **** 3456"),
                                                   ("9876543210987654", "9876 54** **** 7654"),
                                                   ("4567890123456789", "4567 89** **** 6789"),
                                                   ("1111111111111111", "1111 11** **** 1111"),
                                                   ("0000000000000000", "0000 00** **** 0000"),
                                                   ("123456789012345", "Некорректный номер карты"),
                                                   ("12c345678901234a", "Некорректный номер карты")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [("1234567890123456", "**3456"),
                                                   ("9876543210987654", "**7654"),
                                                   ("4567890123456789", "**6789"),
                                                   ("1111111111111111", "**1111"),
                                                   ("0000000000000000", "**0000"),
                                                   ("123456789012345", "Некорректный номер счета"),
                                                   ("12c345678901234a", "Некорректный номер счета")])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected



