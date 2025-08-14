def filter_by_state(list_state: list[dict], key_state: str = "EXECUTED") -> list[dict]:
    """Функция  принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только
    те словари, у которых ключ state соответствует указанному значению."""
    total_state = []
    for i in list_state:
        if i["state"] == key_state:
            total_state.append(i)
    return total_state


def sort_by_date(list_state: list[dict], sorting: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,задающий порядок
    сортировки (по умолчанию — убывание) и возвращает новый список,
    отсортированный по дате (date)."""
    sorted_state = sorted(list_state, key=lambda x: x["date"], reverse=sorting)
    return sorted_state
