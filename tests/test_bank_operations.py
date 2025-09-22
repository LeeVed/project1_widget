from src.bank_operations import process_bank_operations
from src.bank_operations import process_bank_search


def test_process_bank_search() -> None:
    """Функция обрабатывает пустой список"""
    assert process_bank_search([], "string") == []


def test_process_bank_search_match() -> None:
    """Функция обрабатывает совпадение"""
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    search_string = "Перевод организации"
    assert process_bank_search(transactions, search_string) == [{"description": "Перевод организации"}]


def test_process_bank_search_no_matches() -> None:
    """Функция обрабатывает несовпадение"""
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Оплата услуг"},
        {"description": "Открытие вклада"},
    ]
    search_string = "Перевод организации"
    assert process_bank_search(transactions, search_string) == []


def test_process_bank_operations() -> None:
    """Функция обрабатывает пустые списки; пустой список транзакций и список категорий"""
    assert process_bank_operations([], []) == {}
    assert (
        process_bank_operations(
            [], ["Перевод организации", "Открытие вклада", "Перевод с карты на счет", "Перевод с карты на карту"]
        )
        == {}
    )


def test_process_bank_operations_correct_amount() -> None:
    """Функция корректно считает количество категорий"""
    transaction = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на счет"},
        {"description": "Перевод с карты на карту"},
    ]
    category = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
        "Открытие вклада",
        "Перевод с карты на счет",
        "Перевод с карты на карту",
    ]

    assert process_bank_operations(transaction, category) == {
        "Перевод организации": 1,
        "Открытие вклада": 4,
        "Перевод с карты на карту": 4,
        "Перевод с карты на счет": 1,
    }


def test_process_bank_operations_no_match() -> None:
    """Функция корректно обрабатывает случай, когда нет совпадений категорий."""
    transactions = [{"description": "Покупка продуктов"}, {"description": "Оплата услуг"}, {"description": "Зарплата"}]

    categories = ["Перевод организации", "Открытие вклада", "Перевод с карты на карту"]
    assert process_bank_operations(transactions, categories) == {}
