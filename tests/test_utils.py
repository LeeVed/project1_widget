from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import convert_amount
from src.utils import convert_amount_csv_excel
from src.utils import open_json


def test_open_json() -> None:
    assert open_json("") == []
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1":"2"')):
        assert open_json("") == []


def test_convert_amount() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 100}
        assert convert_amount({"operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}}) == 100
        assert convert_amount({"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}) == 1000
        assert convert_amount({}) == "Неверный формат"


def test_convert_amount_csv_excel() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 100}
        assert convert_amount_csv_excel({"amount": "79114.93", "currency_code": "USD"}) == 100
        assert convert_amount_csv_excel({"amount": "1000", "currency_code": "RUB"}) == 1000
        assert convert_amount({}) == "Неверный формат"
