"""
__str__, o método __str__ retorna a representação do objeto em formato string
Este método difere de object.__repr__() por não haver expectativa de que __str__() retorne 
uma expressão Python válida: uma representação mais conveniente ou concisa pode ser usada.
"""

class Example():
    
    def __init__(self, name: str):
        self.__name: str = name
        
    def __repr__(self) -> str:
        return 'Example("{0.name!s}") __repr__'.format(self)
    
    def __str__(self) -> str:
        return f'Example {self.__name} __str__'
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name


example = Example("Candido")
print(example)