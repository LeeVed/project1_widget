import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(currency: str, amount: str) -> Any:
    """Функция обращется к внешнему API и получает текущий курс валют и конвертацию суммы операции в рубли."""
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"

    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers, data={})
    result = response.json().get("result")
    return result
