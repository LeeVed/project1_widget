import json
import logging
from typing import Any
from src.external_api import convert_currency

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def open_json(path: str) -> Any:
    """Функция открывает json файл"""
    logger.info("Запущена функция open_json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            logger.info("Открыт файл")
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка {e}")
        return []
    except FileNotFoundError as e:
        logger.error(f"Ошибка {e}")
        return []
    except Exception as error:
        logger.error(f"Ошибка {error}")
        return []


def convert_amount(dict_list: dict) -> Any:
    """Функция возвращает сумму транзакции в рублях"""
    logger.info("Запущена функция convert_amount")
    try:
        currency = dict_list["operationAmount"]["currency"]["code"]
        amount = dict_list["operationAmount"]["amount"]
        if currency == "RUB":
            logger.info("Успешная транзакция в рублях")
            return float(amount)
        else:
            result = convert_currency(currency, amount)
            logger.info("Успешная конвертация в рубли")
            return round(result, 2)
    except (KeyError, TypeError):
        logger.error("Ошибка: неверный формат")
        return "Неверный формат"
