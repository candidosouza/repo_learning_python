"""
Use o __new__ quando você precisar controlar a criação de uma nova instancia da classe. 
Use o __init__ quando você precisar controlar a inicialização de uma nova instancia.
O __new__ é o primeiro passo da criação de uma instancia. 
Ele é chamado primeiro, e é responsavel por retornar uma nova instancia da sua classe. 
Em contraste, o __init__ não retorna nada, ele é apenas responsável pela inicialização 
da instancia após a classe ser criada.
Em geral, você não deveria sobrepor o __new__ ao menos que seja uma subclasse, um tipo 
imutável como str, int, unicode ou tuple.
"""

class Example():
	def __new__(cls, *args):
		return "ok"

ex = Example()
ex01 = Example("Teste")

print(ex)