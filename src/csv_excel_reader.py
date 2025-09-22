import csv
from typing import Any
from typing import Hashable

import pandas as pd


def read_transaction_csv(file_path: str) -> list[dict[str, str]]:
    """функция считывает финансовые операции из CSV и возвращает список словарей
    с транзакциями"""
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        dictionary_list_csv = []
        for row in reader:
            dictionary_list_csv.append(row)
    return dictionary_list_csv


def read_transaction_excel(file_path: str) -> list[dict[Hashable, Any]]:
    """функция считывает финансовые операции из Excel и выдает список словарей с
    транзакциями."""
    df = pd.read_excel(file_path)
    dictionary_list_excel = df.to_dict(orient="records")
    return dictionary_list_excel
