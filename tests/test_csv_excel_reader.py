from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd

from src.csv_excel_reader import read_transaction_csv
from src.csv_excel_reader import read_transaction_excel


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
