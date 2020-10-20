"""
Composição,  combinação de obj ou classes em estruturas de dados.

"""

class A():
    
    def a1(self) -> str:
        print("Classe A")


class B():
    
    def b(self) -> str:
        print("Classe B")
        A().a1()



composicao = B()
composicao.b()