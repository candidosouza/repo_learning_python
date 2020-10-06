class User():
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts: int = 0
    
    def describe_user(self) -> str:
        print("O email do usuário " + self.first_name.title() + " " + self.last_name.title() + " é: " + self.email)
    
    def greet_user(self) -> str:
        print("Seja bem vindo " + self.first_name.title() + " " + self.last_name.title() + "!")
    
    def increment_login_attempts(self) -> int:
        """ incrementa as tentativas de login """
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> int:
        """ reseta as tentativas de login """
        self.login_attempts = 0
    
    def get_login_attempts(self) -> int:
        """ obtem as tentativas de login """
        return self.login_attempts

print('\n')

user = User("Candido", "Souza", "candido@email.com")
user.describe_user()
user.greet_user()
user.increment_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())
user.reset_login_attempts()
print(user.get_login_attempts())
user.increment_login_attempts()
print(user.get_login_attempts())

print('\n')

# user = User("Felipe", "Bertolin de Souza", "felipe@email.com")
# user.describe_user()
# user.greet_user()

# print('\n')

# user = User("Maria", "Helena de Souza", "maria@email.com")
# user.describe_user()
# user.greet_user()

# print('\n')