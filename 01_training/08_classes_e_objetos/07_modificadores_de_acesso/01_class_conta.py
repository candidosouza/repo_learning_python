class Conta:
    """Simples emxemplo de modelar uma conta bancária"""
    def __init__(self, saldo: float = 0.0):
        self.__saldo: float = saldo
    
    def __repr__(self) -> str:
        return 'Conta({0.saldo!s})'.format(self)
    
    def __str__(self) -> str:
        return 'class Conta({0.saldo!s}):'.format(self)
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def set_saldo(self, saldo: float) -> float:
        if(saldo < 0):
            return f"saldo não pode ser negativo"
        else:
            self.__saldo += saldo


conta = Conta(100)
print(conta.get_saldo())
conta.set_saldo(350.50)
print(conta.get_saldo())
print(conta.set_saldo(-2))
print(conta.get_saldo())

# retirna erro
# conta.__saldo
    
    