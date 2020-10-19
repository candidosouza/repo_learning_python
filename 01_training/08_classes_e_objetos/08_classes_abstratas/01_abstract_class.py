"""
Classes Abstratas, Serve como modelos de base para as sub-classes,
não é possivel instanciar,
obriga todas as sub-classes que a herdam definir os mesmos métodos
"""

import abc

class A(abc.ABC):
    
    @abc.abstractmethod
    def show_info(self) -> str:
        pass
    

class B(A):
    
    def show_info(self) -> str:
        print("Sou a Sub Classe B")


class C(A):
    
    def show_info(self) -> str:
        print("Sou a Sub Classe C")


# class01 = A()
# class01.show_info()

class02 = B()
class02.show_info()

class03 = C()
class03.show_info()
