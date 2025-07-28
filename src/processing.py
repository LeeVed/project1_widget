from datetime import datetime

date_object = datetime.strptime("2023-10-22", "%Y-%m-%d")


def filter_by_state(list_dic: list, state: str = "EXECUTED") -> list:
    """Функция  принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только
    те словари, у которых ключ state соответствует указанному значению."""
    filter_list = []
    for item in list_dic:
        if item.get("state") == state:
            filter_list.append(item)
    return filter_list


def sort_by_date(date_dic_list: list, key_date: str = "date", descending: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и возвращает новый список,
    отсортированный по дате (date)."""
    return sorted(
        date_dic_list, key=lambda x: datetime.strptime(x[key_date], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending
    )


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
