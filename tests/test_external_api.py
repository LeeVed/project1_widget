from unittest.mock import patch
from src.external_api import convert_currency


def test_convert_currency() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 124.01}
        result = convert_currency("USD", "100")
        assert result == 124.01
