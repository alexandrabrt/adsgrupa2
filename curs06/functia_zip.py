# lista_intregi = [1, 2, 3, 4, 5]
# lista_stringuri = ('unu', 'doi', 'trei', 'patru', 'cinci', 'sase')

# rezultat = list(zip(lista_intregi, lista_stringuri))
# print(rezultat)

cifra_de_control = 279146358279
cnp = 1021207430017
print(list(str(cifra_de_control)))
print(list(str(cnp)))
print(list(zip(list(str(cifra_de_control)), list(str(cnp)))))
# print(zip(list(cifra_de_control), cnp))
rezultat = 0
for x, y in list(zip(list(str(cifra_de_control)), list(str(cnp)))):
    rezultat = int(x) * int(y) + rezultat
print(rezultat)
