"""
Decorators, acrecenta conteúdo a fução existente, sem alterar a prória, mas alterando seu comportamento final.
método para envolver uma função, modificando seu comportamento.
"""

from typing import Callable


def decorator(funcao: Callable ) -> str:
    def wrapper() -> str:
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper


@decorator
def funcao_normal() -> str:
    print ("Sou um belo argumento!")

funcao_normal()
