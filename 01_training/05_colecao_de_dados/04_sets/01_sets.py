# -*- coding: utf-8 -*-
"""
Set é uma coleção não ordenada e não indexada.
Não admite elementos repetidos.
Quando criado não é possivel modificar os elementos.
É posivel adicionar elementos.
"""

set01 = {77, "teste", 39, "Candido"}

print(set01)
print('#tipo de set')
print(type(set01))
print('#tamanho')
print(len(set01))
print('#adicionando elemento')
set01.add("Adicionou")
print(set01)
print('#atualizando set')
set01.update([10, 20, "Jose"])
print(set01)
print('#removendo elemento')
set01.discard("Jose")
print(set01)
print('#adicionando todos elemento')
set01.clear()
print(set01)

print('#set remove os repetidos')
a = "Testete"
print(a)
print('#set remove os repetidos')
b = set(a)
print(b)
print(len(b))

x = set("bola")
y = set("cola")

print(x)
print(y)

print('#diferença de x referente ao y:')
print(x - y)
print('#diferença de y referente ao x:')
print(y - x)
print('#união de x e y:')
print(x | y)
print('#interseção de x e y:')
print(x & y)
print('#elementos unicos entre x e y:')
print(x ^ y)
