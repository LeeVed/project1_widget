from unittest.mock import mock_open
from unittest.mock import patch
import pandas as pd
from src.csv_excel_reader import read_transaction_csv
from src.csv_excel_reader import read_transaction_excel
from typing import Any


def test_read_transaction_csv() -> None:
    """Функция обрабатывает пустой файл"""
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        result = read_transaction_csv("path/to/empty.csv")
        assert result == []
        mock_file.assert_called_once_with("path/to/empty.csv", encoding="utf-8")


def test_read_transaction_excel() -> None:
    """Функция обрабатывает пустой файл"""
    with patch("pandas.read_excel", return_value=pd.DataFrame()) as mock_read_excel:
        result = read_transaction_excel("path/to/empty.xlsx")
        assert result == []
        mock_read_excel.assert_called_once_with("path/to/empty.xlsx")


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""id;state;date;amount;currency_name;currency_code;
from;to;description1;EXECUTED;2023-09-05T11:30:32Z;not_a_number;Sol;PEN;Счет 58803664561298323391;
Счет 39745660563456619397;Перевод организации2;;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;
Discover 0720428384694643;Перевод с карты на карту""",
)
def test_incorrect_data_csv(mock_file: Any) -> None:
    """Функция обрабатывает корректность данных csv файла"""
    result = read_transaction_csv("path.to.incorrect.csv")
    assert result == []


@patch("pandas.read_excel")
def test_incorrect_data_excel(mock_read_excel: Any) -> None:
    """Функция обрабатывает корректность данных excel файла"""
    mock_data = pd.DataFrame(
        {
            "id": [1, 2],
            "state": ["EXECUTED", ""],  # Пустое значение
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
            "amount": ["not_a_number", 29740],  # Некорректное значение
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"],
        }
    )
    mock_read_excel.return_value = mock_data
    result = read_transaction_excel("path/to/incorrect.xlsx")
    assert result == []
