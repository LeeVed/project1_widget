import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(dictionary_list, state_canceled, state_executed):
    assert filter_by_state(dictionary_list) == state_executed
    assert filter_by_state(dictionary_list, key_state="CANCELED") == state_canceled


def test_sort_by_date(dictionary_list, sort_true, sort_false):
    assert sort_by_date(dictionary_list) == sort_true
    assert sort_by_date(dictionary_list, sorting=False) == sort_false