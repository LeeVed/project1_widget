from typing import Any

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


@log()
def add_console(x: int, y: int) -> int:
    """Тест успешного выполнения с выводом в консоль"""
    return x + y


def test_log_success_console(capsys: CaptureFixture[str]) -> None:
    add_console(1, 2)
    captured = capsys.readouterr()
    assert "add_console ok. Result: 3\n" == captured.out


def test_log_error_console(capsys: CaptureFixture[str]) -> None:
    """Тест на вывод ошибки в консоль"""
    with pytest.raises(TypeError):
        add_console(5, "x")  # type: ignore
    captured = capsys.readouterr()
    assert "add_console error: <class 'TypeError'>. args: (5, 'x'), kwargs: {}\n" == captured.out


file_name = "tests/mylog.txt"


@log(filename=file_name)
def add(x: int, y: int) -> Any:
    return x + y


def test_addition() -> None:
    """Тест сложения аргументов"""
    result = add(5, 6)
    assert result == 11


@log(filename=file_name)
def add_file(x: Any, y: Any) -> Any:
    return x + y


def test_log_success_file() -> None:
    """Тест успешного выполнения с записью в файл:"""
    add_file(3, 4)
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.readlines()
        assert "add_file ok" in contents[-1]


@log(filename=file_name)
def faulty_function(x: int, y: int) -> Any:
    return x / y


def test_log_error_file() -> None:
    """Тест вывода ошибки с записью в файл:"""
    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.readlines()
        assert "faulty_function error: <class 'ZeroDivisionError'>. args: (1, 0), kwargs: {}" in contents[-1]
