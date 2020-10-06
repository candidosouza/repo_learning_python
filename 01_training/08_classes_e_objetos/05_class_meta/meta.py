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
    
    class Meta:
        # armazena informações extras
        verbose_name_plural = 'cars'