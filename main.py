from src.bank_operations import process_bank_search
from src.csv_excel_reader import read_transaction_csv
from src.csv_excel_reader import read_transaction_excel
from src.generators import filter_by_currency
from src.generators import filter_by_currency_csv_excel
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import open_json
from src.widget import get_date
from src.widget import mask_account_card

if __name__ == "__main__":

    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    user_input_choice = input(":")
    while user_input_choice not in ["1", "2", "3"]:
        print("Некорректно введен пункт меню. Выберите цифру от 1 до 3")
        user_input_choice = input(":")
    if user_input_choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = open_json("data/operations.json")
    elif user_input_choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_transaction_csv("data/transactions.csv")
    elif user_input_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transaction_excel("data/transactions_excel.xlsx")

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    user_input = input(":").upper()

    while user_input not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции '{user_input}' недоступен.")

        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_input = input(":").upper()
    transactions = filter_by_state(transactions, key_state=user_input)
    print(f"Операции отфильтрованы по статусу {user_input}")

    user_input = input("Отсортировать операции по дате? Да/Нет\n:").lower()
    if user_input == "да":
        user_input = input("Отсортировать по возрастанию или по убыванию?\n:")
        if user_input == "по возрастанию":
            sorting = False
        else:
            sorting = True
        transactions = sort_by_date(transactions, sorting=sorting)

    user_input = input("Выводить только рублевые транзакции?\n:").lower()
    if user_input_choice in ["2", "3"]:
        if user_input == "да":
            transactions = list(filter_by_currency_csv_excel(transactions, "RUB"))
    else:
        if user_input == "да":
            transactions = list(filter_by_currency(transactions, "RUB"))

    user_input = input("Отфильтровать список транзакций по определенному слову в описании?\n:").lower()
    if user_input == "да":
        user_input = input("Введите слово для фильтрации\n:")
        transactions = process_bank_search(transactions, user_input)

    operations_quantity = len(transactions)
    if operations_quantity == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций")
        print(f"Всего банковских операций в выборке: {operations_quantity}")
        for item in transactions:
            correct_date = get_date(item["date"])
            print(f"{correct_date} {item["description"]}")
            mask_card_to = mask_account_card(item["to"])
            if item.get("from"):
                print(mask_card_to)
            else:
                mask_card_from = mask_account_card(item["from"])
                print(f"{mask_card_from} -> {mask_card_to}")
            if user_input_choice in ["2", "3"]:
                print(f"Сумма: {item["amount"]} {item["currency_code"]}")
            else:
                print(f"Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["code"]}")
            print()
