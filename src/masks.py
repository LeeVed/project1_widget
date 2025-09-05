import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Запущена функция get_mask_card_number")
    if len(card_number) == 16 and card_number.isdigit():
        mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.info("Успешно введен номер карты")
        return mask_number
    logger.error("Введен некоррректный номер карты")
    return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.info("Запущена функция get_mask_account")
    if len(account_number) == 20 and account_number.isdigit():
        mask_account = f"**{account_number[-4:]}"
        logger.info("Успешно введен номер счета")
        return mask_account
    logger.error("Введен некоррректный номер счета")
    return "Некорректный номер счета"
