import pytest


@pytest.fixture
def dictionary_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def state_canceled() -> list:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def state_executed() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_true() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_false() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def transaction_usd() -> list:
    return [
        {"id": 1, "operationAmount": {"amount": "150", "currency": {"code": "USD"}}},
        {"id": 3, "operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
    ]


@pytest.fixture
def transactions_other_currency() -> list:
    return [{"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}}]


@pytest.fixture
def transactions_no_usd() -> list:
    return [
        {"id": 4, "operationAmount": {"amount": "500", "currency": {"code": "EUR"}}},
        {"id": 5, "operationAmount": {"amount": "1000", "currency": {"code": "GBP"}}},
    ]


@pytest.fixture
def transactions_empty_list() -> list:
    return []


@pytest.fixture
def transactions_data() -> list:
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод с карты на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод со счета на карту"},
        {"id": 5, "description": "Перевод с карты на карту"},
    ]
