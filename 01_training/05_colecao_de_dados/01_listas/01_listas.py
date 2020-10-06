"""
lista, conjuntos de vários tipos de dados
relação de valores
["valor"]
são mutáveis, podem mudar
"""

lista1 = [30, 20, 10, 30]
lista2 = ["carro", "moto", "avião", "caminhão"]
lista3 = [10, "carro", 77.7, "moto", 33.3333]

print('#listas')
print(lista1)
print(lista2)
print(lista3)

print('#tipos')
print(type(lista1))
print(type(lista2))
print(type(lista3))

print('#tamanhos')
print(len(lista1))
print(len(lista2))
print(len(lista3))

print('#elementos expecíficos')
print(lista1[0])
print(lista1[0:2])
print(lista1[-1])

print('# append(valor), adicionando elementos no final da lista')
print(lista1)
lista1.append(77)
print(lista1)

print('# insert(index, valor), adicionando elementos no index desejado')
lista1.insert(0, 15)
print(lista1)

print('# pop(index), remove elementos no index desejado')
lista1.pop(0)
print(lista1)

print('# remove(valor), remove elementos com o valor desejado')
lista1.remove(77)
print(lista1)

print('# clear(), apaga todos elementos da lista')
lista1.clear()
print(lista1)

print('# extend(list), adicionas todos elementos de outra lista')
lista1 = [30, 20, 10, 30]
lista1.extend(lista2)
print(lista1)


print('# reverse(), inverte os elementos da lista')
lista1.reverse()
print(lista1)

print('# sort(), ordena os elementos da lista')
print('# sort(), não aceita elementos de tipos diferentes, com int e str por ex.')
print("not supported between instances of 'int' and 'str', os elementos tem q ser sempre dos mesmos tipos")
a = [30, 20, 10, 30]
a.sort()
print(a)

print('# list.index(valor), retorna a posição do valor inserido, iniciando pelo index 0')
b = [30, "candido", 10, 30, 77.7]
c = b.index(10)
print(c)

print('# list.copy(), copia um lista')
e = lista2.copy()
print(e)

print('# list.count(valor), conta quantas vezes aparece o valor desejado')
f = lista2.count("carro")
print(f)
