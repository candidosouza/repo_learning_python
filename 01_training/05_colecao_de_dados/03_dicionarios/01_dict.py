"""
dicionários, coleção indexada
mas não ordenada
relação de chaves e valores (key and value)
chaves associados as valores
"""

dict1 = {
    "Marca": "Ferrari",
    "Ano": 2020,
    "Cor": "Vermelho",
    "Motor": 6.0
}

print('# dicionários')
print(dict1)

print('# tipo - type(dict)')
print(type(dict1))

print('# tamanho - len(dict)')
print(len(dict1))

print('# elementos expecíficos - dict.get(chave)')
print(dict1.get("Ano"))
print(dict1.get("Marca"))

print('# Alterando elementos - dict[chave] = valor')
dict1["Cor"] = "Azul"
print(dict1)

print('# Adicionando elementos - dict[chave] = valor')
dict1["Vidros"] = "Elétricos"
print(dict1)

print('# Removendo elementos - dict.pop(chave) / del dict[chave]')
dict1.pop("Vidros")
print(dict1)
del dict1["Cor"]
print(dict1)

print('# Removendo a última chave - dict.popitem()')
dict1.popitem()
print(dict1)

print('# Removendo todos elementos do dicionário - dict.clear()')
dict1.clear()
print(dict1)


dict2 = {
    "Marca": "Ford",
    "Ano": 2020,
    "Cor": "Vermelho",
    "Motor": 3.0
}

print('# Obtendo somente as chaves do dicionário - dict.keys()')
print(dict2.keys())

print('# Obtendo somente os valores do dicionário - dict.values()')
print(dict2.values())

print('# Obtendo os pares do dicionário - dict.values()')
print(dict2.items())

print('# loop')

for key, value in dict2.items():
    print(key, value)


print('# verificando se uma chave existe no cicionário')
if "Marca" in dict2:
    print("a chave existe")

# ou
# if "Marca" in dict2.keys():

print('# verificando se uma valor existe no cicionário')
if "Ford" in dict2.values():
    print("o valor existe")





