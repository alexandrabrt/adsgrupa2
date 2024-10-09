# def suma(x, y):
#     return x + y
#
#
# rezultat = suma(1, 2)
# print(rezultat)

# suma = lambda x, y: x + y
# rezultat = suma(1, 2)
# print(rezultat)

jucatori = [{
        "nume": "Popescu",
        "prenume": "Ion",
        "varsta": 21
    },
    {
        "nume": "Marin",
        "prenume": "Andreea",
        "varsta": 42
    },
    {
        "nume": "Ionescu",
        "prenume": "Maria",
        "varsta": 14
    }]

sortare_valori = sorted(jucatori, key=lambda valoare: valoare['varsta'], reverse=True)
print(sortare_valori)
