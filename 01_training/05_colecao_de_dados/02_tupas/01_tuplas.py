"""
Tuplas é uma coleção indexada.
Não é possivel alterar seus valores.
Não é possivel adicionar, alterar, remover os itens.
são imutáveis, não podem mudar
"""

tupla1 = (10, "carro", 20, 30, 10)
tupla2 = 20, 75, 15

print('#tipo de tupla')
print(type(tupla1))
print(type(tupla2))

print('#elementos')
print(tupla1)
print(tupla2)

print('# indexando elemento expecifico')
print(tupla1[1])
print(tupla1[0])
print(tupla1[0:2])
print(tupla1[-1])

print('# tamanho')
print(len(tupla1))

print('# count - número de vezes q o elemento aparece')
print(tupla1.count(10))

print('# index - posição do elemento')
print(tupla1.index(30))

print('# Não pode alterar elemento, porém pode converter em lista para alterar')
# tupla1[0] = 15
print(tupla1)
convert_list = list(tupla1)
convert_list[0] = 15
tupla1 = tuple(convert_list)
print(tupla1)
