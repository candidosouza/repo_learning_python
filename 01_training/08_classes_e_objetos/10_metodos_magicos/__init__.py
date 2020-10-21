"""
__init__, o método __init__ não retorna nada, ele é apenas responsável pela inicialização 
da instancia após a classe ser criada.
Use o __init__ quando você precisar controlar a inicialização de uma nova instancia.
"""

class MethodMagicInit():
    
    def __init__(self, name: str):
        self.__name: srt = name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name


method_init = MethodMagicInit("Candido")
print(method_init.name)