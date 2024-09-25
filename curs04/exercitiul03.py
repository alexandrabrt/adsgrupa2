lista = [10, 13, 2, 6, 14]

suma = None
for index, element in enumerate(lista):
    if index != len(lista) - 1:
        suma = element + lista[index + 1]
        print(suma)
