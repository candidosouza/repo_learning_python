from typing import AnyStr, Callable

# aceitas outras funções como argumentos
def funcao01(a: Callable) -> None:
    print("Dentro da função 01")
    print(a.__name__)
    a()


def funcao02() -> str:
    print("Dentro da função 02")

#funcao01()
funcao02()
funcao01(funcao02)
