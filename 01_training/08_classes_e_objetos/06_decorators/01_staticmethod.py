class Car:
    """Simples temtativa de modelar um usuário"""

    # atributos da classe
    pneus: str = 'Default'

    def __init__(self, make: str, model: str, year: int):
        # atributos da instância
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading: int = 0


instancia_car = Car("audi", "a4", 2020)
pneus = Car("audi", "a4", 2020).pneus
pneus2 = instancia_car.pneus

print(pneus)
print(Car("audi", "a4", 2020))
print(pneus2)
