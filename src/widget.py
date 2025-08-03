from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """Функция принимает на вход строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером"""
    index_digit = card_account_number.rfind(" ")
    if "Счет" in card_account_number[:index_digit]:
        mask_account = get_mask_account(card_account_number[index_digit + 1:])
        return card_account_number[: index_digit + 1] + mask_account
    else:
        mask_card_number = get_mask_card_number(card_account_number[index_digit + 1:])
        return card_account_number[: index_digit + 1] + mask_card_number


def get_date(data_str: str) -> str:
    """Функция принимает строку и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    date = data_str[:10]
    date_split = date.split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_mask_account("73654108430135874305"))
    print(get_mask_card_number("1234567812345678"))
