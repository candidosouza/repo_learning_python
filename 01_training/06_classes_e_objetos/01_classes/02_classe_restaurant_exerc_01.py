class Restaurant():

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served: int = 0
    
    def describe_restaurant(self) -> str:
        print("Restaurante " + self.restaurant_name.title() + ", cozinha " + self.cuisine_type + ".")
    
    def open_restaurant(self) -> str:
        print("O Restaurante " + self.restaurant_name.title() + " está aberto!")
    
    def set_number_served(self, number: int) -> int:
        if number >= self.number_served:
            self.number_served = number
        else:
            print("erro, o número fornecido é menor que o total de cliente")
    
    def get_number_served(self) -> str:
        print("O total de clientes servidos é " + str(self.number_served))
    
    def increment_number_served(self, number: int) -> int:
        if number >= 0:
            self.number_served += number
        else:
            print("erro, o número fornecido é menor que o total de cliente")



print('\n')

restaurant = Restaurant("Dú chef", "italiana")
print("Nome do restaurante: " + restaurant.restaurant_name.title())
print("Comida servida do tipo: " + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(77)
restaurant.get_number_served()
restaurant.increment_number_served(3)
restaurant.get_number_served()
restaurant.increment_number_served(-55)
restaurant.get_number_served()
restaurant.set_number_served(2)
restaurant.get_number_served()
print('\n')

# restaurant1 = Restaurant("BonJour", "Francesa")
# restaurant1.describe_restaurant()

# print('\n')

# restaurant2 = Restaurant("Halim", "árabe")
# restaurant2.describe_restaurant()

# print('\n')

# restaurant3 = Restaurant("Takanakara", "japonesa")
# restaurant3.describe_restaurant()

# print('\n')
