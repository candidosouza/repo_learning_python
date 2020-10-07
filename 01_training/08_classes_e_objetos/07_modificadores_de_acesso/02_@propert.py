class Conta:
    """Simples emxemplo de modelar uma conta bancária"""
    def __init__(self, saldo: float = 0.0):
        self._saldo: float = saldo
    
    def __repr__(self) -> str:
        return 'Conta({0.saldo!s})'.format(self)
    
    def __str__(self) -> str:
        return 'class Conta({0.saldo!s}):'.format(self)
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo: float) -> float:
        if(saldo < 0):
            # return f"saldo não pode ser negativo"
            print("saldo não pode ser negativo")
        else:
            self._saldo += saldo


conta = Conta(100)
print(conta.saldo)
conta.saldo = 350.50
print(conta.saldo)
conta.saldo = -20
print(conta.saldo)

print(conta)

# retorna erro
# conta.__saldo