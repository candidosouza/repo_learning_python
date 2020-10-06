"""
Decorators, acrecenta conteúdo a fução existente, sem alterar a prória
"""

def fucao_decorator() -> str:
    print("Funçao deocorator")


@funcao_decorator
def funcao_normal() -> str:
    print("Função Normal")
