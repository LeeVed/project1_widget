import pandas as pd
import csv
from typing import Any, Hashable


def read_transaction_csv(file_path: str) -> list[dict[str, str]]:
    """функция считывает финансовые операции из CSV и возвращает список словарей
    с транзакциями"""
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        dictionary_list_csv = []
        for row in reader:
            try:
                for key, value in row.items():
                    if value == "":
                        return []
            except ValueError as e:
                print(f"Ошибка данных: {e}")
                continue
            dictionary_list_csv.append(row)
        if not dictionary_list_csv:
            print("Warning: Файл пустой")
    return dictionary_list_csv


def read_transaction_excel(file_path: str) -> list[dict[Hashable, Any]]:
    """функция считывает финансовые операции из Excel и выдает список словарей с
    транзакциями."""
    df = pd.read_excel(file_path)
    dictionary_list_excel = df.to_dict(orient="records")
    for row in dictionary_list_excel:
        for key, value in row.items():
            if value == "":
                return []
            if key == "amount":
                try:
                    int(value)
                except ValueError:
                    print(f"Warning: Некорректное значение в поле '{key}'")
    if df.empty:
        print("Warning: Файл пустой")
    return dictionary_list_excel
