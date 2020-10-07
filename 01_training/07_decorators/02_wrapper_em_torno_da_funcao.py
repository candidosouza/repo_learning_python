"""
Colocar um wrapper em torno de uma função, para adicionar um processamento extra
wrapper(encapsulador)
"""

import time
from typing import Callable
from functools import wraps


def runtime(func: Callable) -> Callable:
    """
    Decorator que informa o tempo de execução
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> float:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start, "ms")
        return result
    
    return wrapper


@runtime
def countdown(n: int) -> None:
    """
    Faz uma contagem decrescente
    """
    while n > 0:
        n -= 1
        print(n)


countdown(10)
