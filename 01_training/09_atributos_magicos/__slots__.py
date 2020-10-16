""" __slots__, limita os atributos da classe,
    limita os atributos na sua criação, não deixa criar atributos após sua criação
"""


class Dog():
    """ Uma tentativa simples de modelar um cachorro """

    def __init__(self, name: str, age: int):
        """ inicializa os atributos name e age """
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        """ Altera a representação de uma instância, converte para string """
        return 'Dog({0.name!s}, {0.age!s})'.format(self)
    
    def __str__(self) -> str:
        """ Altera a representação de uma instância, converte para string """
        return '({0.name!s}, {0.age!s})'.format(self)
    
    def sit(self) -> str:
        """ Simula um cachorro sentado em resposta a um comando """
        print(self.name.title() + " is now setting.")
    
    def roll_over(self) -> str:
        """ Simula um cachorro rolando em resposta a um comando """
        print(self.name.title() + " rolled over!")


my_dog = Dog("Willie", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
my_dog
print(my_dog)
"""
Atributo color criado depois da sua instância, o __slot__ evita isso.
Não existe esse atributo na classe criada
"""
my_dog.color = "Black"
print(my_dog.color )


"""Exemplo de classe com __slots__"""
class Bird():
    """
    Simples temtativa de criar um pássaro
    """
    
    __slots__ = ['__type']
    
    def __init__(self, type: str):
        """Inicializa o atributo type"""
        self.__type: str = type
    
    
    @property
    def type(self) -> str:
        return self.__type
    
    @type.setter
    def type(self, type: str):
        self.__type = type


bird = Bird("Calopsita")
print(bird.type)
"""
Com slots definido na classe, não é permitido a criação de atributos depois da instancia,
isso acarretará em erro...
"""
bird.color = 'Black'
print(bird.color)