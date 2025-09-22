import re
from collections import Counter


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска и
    возвращает список словарей, у которых в описании есть данная строка."""
    if not data:
        return []
    filtered_list = []
    for transaction in data:
        if transaction.get("description") and re.search(
            search_string, transaction["description"], flags=re.IGNORECASE
        ):
            filtered_list.append(transaction)
    return filtered_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """функция принимет список словарей с данными о банковских операциях и список категорий операций и
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    if not data:
        return {}
    counted_categories: Counter = Counter()
    for transaction in data:
        description = transaction.get("description", "")
        for category in categories:
            if category in description:
                counted_categories[category] += 1

    return dict(counted_categories)
