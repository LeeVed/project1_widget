import pytest
from src.decorators import log

# Тест успешного выполнения с выводом в консоль:
@log()
def add_console(x, y):
    return x + y


def test_log_success_console(capsys):
    add_console(1, 2)
    captured = capsys.readouterr()
    assert "add_console ok" in captured.out

# Тест на вывод ошибки в консоль
@log()
def faulty_add(x, y):
    return x + str(y)


def test_log_error_console(capsys) -> None:
    with pytest.raises(TypeError):
        faulty_add(5, "x")
    captured = capsys.readouterr()
    assert "faulty_add error: <class 'TypeError'>. args: (5, 'x'), kwargs: {}\n" in captured.out

file_name = "../tests/mylog.txt"

# Тест сложения аргументов
@log(filename=file_name)
def add(x, y):
    return x + y

def test_addition() -> int:
    result = add(5, 6)
    assert result == 11

# Тест успешного выполнения с записью в файл:
@log(filename=file_name)
def add_file(x, y):
    return x + y


def test_log_success_file():
    add_file(3, 4)
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.readlines()
        assert "add_file ok" in contents[-1]

# Тест вывода ошибки с записью в файл:
@log(filename=file_name)
def faulty_function(x, y):
    return x / y


def test_log_error_file():
    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)
    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.readlines()
        assert "faulty_function error: <class 'ZeroDivisionError'>. args: (1, 0), kwargs: {}" in contents[-1]
