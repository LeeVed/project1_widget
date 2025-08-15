from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(dictionary_list: list, state_canceled: str, state_executed: str) -> None:
    assert filter_by_state(dictionary_list) == state_executed
    assert filter_by_state(dictionary_list, key_state="CANCELED") == state_canceled


def test_sort_by_date(dictionary_list: list, sort_true: list, sort_false: list) -> None:
    assert sort_by_date(dictionary_list) == sort_true
    assert sort_by_date(dictionary_list, sorting=False) == sort_false
