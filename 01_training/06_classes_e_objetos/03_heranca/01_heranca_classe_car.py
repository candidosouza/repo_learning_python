
class Car():
    
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading: int = 0
    
    def __repr__(self) -> str:
        return 'Car({0.make!s}, {0.model!s}, {0.year!s})'.format(self)
    
    def __str__(self) -> str:
        return 'class Car({0.make!s}, {0.model!s}, {0.year!s}):'.format(self)
    
    def get_descriptive_name(self) -> str:
        log_name = str(self.year) + " " + self.make + " " + self.model
        return log_name.title()
    
    def read_odometer(self) -> str:
        return "This car has {} miles on int.".format(self.odometer_reading)
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            return "You can't roll back an odometer!"
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            return "You can't roll back an odometer!"


class Battery():

    def __init__(self, batery_size=70):
        self.batery_size = batery_size
    
    def __repr__(self) -> str:
        return 'Batery({0.batery_size!s}'.format(self)
    
    def __str__(self) -> str:
        return 'class Batery({0.batery_size!s}'.format(self)
    
    def describe_batery(self) -> str:
        # return "".join(["This car has a " + str(self.batery_size) + "-kwh battery"])
        return "This car has a {}-kwh battery".format(self.batery_size)


class EletricCar(Car):
    """ representa aspectos de um carro específicos de veículos el """

    def __init__(self, make: str, model: str, year: int, test: bool):
        """ inicia os atributos da classe pai """
        super().__init__(make, model, year)
        self.test = test
        self.batery_model: str = "foo"
        self.battery: int = Battery()
    
    def __repr__(self) -> str:
        return 'EletricCar({0.make!s}, {0.model!s}, {0.year!s}, {0.test!s}):'.format(self)
    
    def __str__(self) -> str:
        return 'Class EletricCar({0.make!s}, {0.model!s}, {0.year!s}, {0.test!s}):'.format(self)
    
    def get_batery_model(self) -> str:
        return self.batery_model

    @staticmethod
    def teste():
        return "ok"

print('\n')

my_tesla = EletricCar("tesla", "model's", 2020, True)
print(my_tesla.get_descriptive_name())
print(my_tesla.get_batery_model())
print(my_tesla.battery.describe_batery())

print('\n')

print(my_tesla)

print('\n')