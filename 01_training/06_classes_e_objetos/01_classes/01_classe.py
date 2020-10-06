
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
