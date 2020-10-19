"""
Herança multipla, é aceita em python,
caso as classes tenham os mesmo método, prevalecerá a colocada em primeiro lugar
"""

class A():
    
    def info(self) -> str:
        print("Hedada da A")


class B():
    
    def info(self) -> str:
        print("Hedada da B")


class C(A, B):
    
    def __init__(self):
        self.init = True


heranca = C()
heranca.info()