"""
__repr__, o método __repr__ retorna a representação do objeto em formato string
"""

class Example():
    
    def __init__(self, name: str):
        self.__name: str = name
    
    def __repr__(self) -> str:
        return 'Example("{0.name!s}")'.format(self)
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name


example = Example("Candido")
print(example)