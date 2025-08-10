def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) == 16 and card_number.isdigit():
        mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return mask_number
    return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if len(account_number) == 20 and account_number.isdigit():
        mask_account = f"**{account_number[-4:]}"
        return mask_account
    return "Некорректный номер счета"
