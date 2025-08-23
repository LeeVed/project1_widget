from time import time
import os
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """ Функция-декоратор, которая автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def decorator(func: Callable) -> Callable:
         def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok. Result: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result

            except Exception as e:
                message = f"{func.__name__} error: {type(e)}. args: {args}, kwargs: {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise

         return wrapper

    return decorator
