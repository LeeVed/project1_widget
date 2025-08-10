from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """Функция принимает на вход строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером"""
    index_digit = card_account_number.rfind(" ")
    if "Счет" in card_account_number[:index_digit]:

        if card_account_number[-20:].isdigit():
            mask_account = get_mask_account(card_account_number[index_digit + 1 :])
            return card_account_number[: index_digit + 1] + mask_account
        else:
            return "Некорректный номер счета"
    else:
        if card_account_number[-16:].isdigit():
            mask_card_number = get_mask_card_number(card_account_number[index_digit + 1 :])
            return card_account_number[: index_digit + 1] + mask_card_number
        else:
            return "Некорректный номер карты"

#         mask_account = get_mask_account(card_account_number[index_digit + 1:])
#         return card_account_number[: index_digit + 1] + mask_account
#     else:
#         mask_card_number = get_mask_card_number(card_account_number[index_digit + 1:])
#         return card_account_number[: index_digit + 1] + mask_card_number



def get_date(data_str: str) -> str:
    """Функция принимает строку и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    date = data_str[:10]
    date_split = date.split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"
