import json
from typing import Any

from src.external_api import convert_currency


def open_json(path: str) -> Any:
    """Функция открывает json файл"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(e)
        return []
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as error:
        print(error)
        return []


def convert_amount(dict_list: dict) -> Any:
    """Функция возвращает сумму транзакции в рублях"""
    try:
        currency = dict_list["operationAmount"]["currency"]["code"]
        amount = dict_list["operationAmount"]["amount"]
        if currency == "RUB":
            return float(amount)
        else:
            result = convert_currency(currency, amount)
            return round(result, 2)
    except (KeyError, TypeError):
        return "Неверный формат"
