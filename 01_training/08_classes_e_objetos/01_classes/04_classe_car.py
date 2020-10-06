
class Car():
    
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading: int = 0
    
    def get_description_name(self) -> str:
        log_name = str(self.year) + " " + self.make + " " + self.model
        return log_name.title()
    
    def read_odometer(self) -> str:
        print("This car has " + str(self.odometer_reading) + " miles on int.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
            


print('\n')

my_my_car = Car("audi", "a4", 2020)
print(my_car.get_description_name())
my_car.update_odometer(777)
my_car.read_odometer()

print('\n')

my_car.increment_odometer(77)
my_car.read_odometer()

print('\n')
